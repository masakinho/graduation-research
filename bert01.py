import torch
import torch.nn as nn
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import pandas as pd
from tqdm import tqdm
from torch.utils.data.dataset import random_split

# デバイスの設定
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# BERTモデルのロード
class BinaryClassifier(nn.Module):
    def __init__(self, num_classes=2):
        super(BinaryClassifier, self).__init__()
        self.bert = BertForSequenceClassification.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking", num_labels=num_classes)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        return outputs.logits

# データセットクラス
class BinaryClassificationDataset(Dataset):
    def __init__(self, data, tokenizer, max_len=128):
        self.tokenizer = tokenizer
        self.max_len = max_len
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        utterance = self.data.loc[idx, "text"]
        label = self.data.loc[idx, "label"]

        input_dict = self.tokenizer(
            utterance,
            max_length=self.max_len,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )
        # 修正: ラベルが1（言語的皮肉）または0（状況的皮肉）の場合にのみ損失を計算
        if label == 1 or label == 0:
            input_dict["labels"] = torch.tensor(label)
        else:
            input_dict["labels"] = torch.tensor(-100)  # ラベルが無効な場合は-100を指定

        return input_dict, label

# モデルの初期化
model = BinaryClassifier().to(device)

# 損失関数と最適化関数の設定
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)

# 正例のデータセット読み込み
csv_file_path_positive = "/home/ishi0826/Downloads/newpos.csv"
df_positive = pd.read_csv(csv_file_path_positive)

# 負例のデータセット読み込み
csv_file_path_negative = "/home/ishi0826/Downloads/newneg.csv"
df_negative = pd.read_csv(csv_file_path_negative)

# 正例と負例のデータフレームを連結
df = pd.concat([df_positive, df_negative], ignore_index=True)

# BERTトークナイザーのロード
tokenizer = BertTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")

# データセットの作成
dataset = BinaryClassificationDataset(df, tokenizer)

# データセットを訓練データとテストデータに手動で分割
total_samples = len(dataset)
train_size = int(0.8 * total_samples)
test_size = total_samples - train_size
train_data, test_data = random_split(dataset, [train_size, test_size])

# データローダーの作成
batch_size = 8
train_dataloader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=batch_size, shuffle=False)

# 学習
num_epochs = 3
for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    for batch in tqdm(train_dataloader, desc=f"Epoch {epoch + 1}/{num_epochs}"):
        inputs, labels = batch
        input_ids = inputs["input_ids"].squeeze(dim=1).to(device)
        attention_mask = inputs["attention_mask"].squeeze(dim=1).to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    average_loss = total_loss / len(train_dataloader)
    print(f"Epoch {epoch + 1}/{num_epochs}, Average Loss: {average_loss:.4f}")

# テスト
model.eval()
all_labels = []
all_preds = []

with torch.no_grad():
    for batch in tqdm(test_dataloader, desc="Testing"):
        inputs, labels = batch
        input_ids = inputs["input_ids"].squeeze(dim=1).to(device)
        attention_mask = inputs["attention_mask"].squeeze(dim=1).to(device)
        labels = labels.to(device)

        outputs = model(input_ids, attention_mask)
        _, predicted = torch.max(outputs, 1)

        all_labels.extend(labels.cpu().numpy())
        all_preds.extend(predicted.cpu().numpy())

# 評価メトリクスの計算
accuracy = accuracy_score(all_labels, all_preds)
precision, recall, f1, _ = precision_recall_fscore_support(all_labels, all_preds, average="binary")

print(f"Test Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
