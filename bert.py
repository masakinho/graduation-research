import torch
import torch.nn as nn
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import pandas as pd
from tqdm import tqdm

# デバイスの設定
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# BERTモデルのロード
class SarcasmClassifier(nn.Module):
    def __init__(self, num_classes=2):
        super(SarcasmClassifier, self).__init__()
        self.bert = BertForSequenceClassification.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking", num_labels=num_classes)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        return outputs.logits

# データセットクラス
class ConversationDataset(Dataset):
    def __init__(self, data, tokenizer, max_len=128):
        self.tokenizer = tokenizer
        self.max_len = max_len

        # conversation_idごとにデータをグループ化
        self.conversations = data.groupby("conversation_id")

    def __len__(self):
        return len(self.conversations)

    def __getitem__(self, idx):
        conversation_id, conversation_data = self.conversations.nth(idx)

        # 会話内の各発言を取得
        utterances = conversation_data["utterance"].tolist()
        labels = conversation_data["label"].tolist()

        # 会話内の各発言に対してデータを作成
        inputs = []
        for utterance, label in zip(utterances, labels):
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
            inputs.append(input_dict)

        return inputs, labels[0]  # 会話IDごとのラベルも返す

# モデルの初期化
model = SarcasmClassifier().to(device)

# 損失関数と最適化関数の設定
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)

# データの読み込み
csv_file_path = "your_dataset.csv"  # ファイルパスを適切に設定
df = pd.read_csv(csv_file_path)

# BERTトークナイザーのロード
tokenizer = BertTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")

# データセットの作成
dataset = ConversationDataset(df, tokenizer)

# 訓練データとテストデータに分割
train_data, test_data = train_test_split(dataset, test_size=0.2, random_state=42)

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
        inputs, conversation_label = batch
        for input_dict in inputs:
            input_ids = input_dict["input_ids"].squeeze(dim=1).to(device)
            attention_mask = input_dict["attention_mask"].squeeze(dim=1).to(device)
            labels = input_dict["labels"].to(device)

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
        inputs, conversation_label = batch
        for input_dict in inputs:
            input_ids = input_dict["input_ids"].squeeze(dim=1).to(device)
            attention_mask = input_dict["attention_mask"].squeeze(dim=1).to(device)
            labels = input_dict["labels"].to(device)

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
