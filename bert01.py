import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import AdamW
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.model_selection import train_test_split

# データセットクラスの定義
class TextDataset(Dataset):
    def __init__(self, dataframe, tokenizer, max_len):
        self.data = dataframe
        self.text = self.data.text
        self.labels = self.data.label
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.text)

    def __getitem__(self, idx):
        text = str(self.text[idx])
        labels = int(self.labels[idx])

        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_len,
            return_token_type_ids=False,
            padding='max_length',  # この行を確認
            truncation=True,       # この行を追加
            return_attention_mask=True,
            return_tensors='pt',
        )

        return {
            'text': text,
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(labels, dtype=torch.long)
        }

# パラメータ設定
MAX_LEN = 128
BATCH_SIZE = 16
EPOCHS = 3

# トークナイザーとモデルの初期化
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# データセットの準備
# CSVファイルを読み込む
pos_data = pd.read_csv('/home/ishi0826/Templates/graduation-research/pst.csv')
neg_data = pd.read_csv('/home/ishi0826/Templates/graduation-research/ngt.csv')

# テキスト中の '\n' を改行文字に置換
pos_data['text'] = pos_data['text'].replace(r'\\n', '\n', regex=True)
neg_data['text'] = neg_data['text'].replace(r'\\n', '\n', regex=True)

data = pd.concat([pos_data, neg_data])

# 訓練データセットとバリデーションデータセットに分割
train_data, val_data = train_test_split(data, test_size=0.2)
train_data = train_data.reset_index(drop=True)  # インデックスをリセット
val_data = val_data.reset_index(drop=True)      # インデックスをリセット

# データセットの準備
train_dataset = TextDataset(train_data, tokenizer, MAX_LEN)
val_dataset = TextDataset(val_data, tokenizer, MAX_LEN)

# データローダーの設定
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)

# オプティマイザーの設定
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)

# 訓練ループ
for epoch in range(EPOCHS):
    model.train()
    for batch in train_loader:
        optimizer.zero_grad()
        input_ids = batch['input_ids']
        attention_mask = batch['attention_mask']
        labels = batch['labels']
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

def evaluate(model, data_loader):
    model.eval()
    predictions, true_labels, misclassified_samples = [], [], []
    with torch.no_grad():
        for batch in data_loader:
            input_ids = batch['input_ids']
            attention_mask = batch['attention_mask']
            labels = batch['labels']
            texts = batch['text']
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            batch_predictions = torch.argmax(logits, dim=1).tolist()
            predictions.extend(batch_predictions)
            true_labels.extend(labels.tolist())

            # 誤分類されたサンプルを特定
            for text, true_label, pred_label in zip(texts, labels, batch_predictions):
                if true_label != pred_label:
                    misclassified_samples.append((text, true_label, pred_label))

    accuracy = accuracy_score(true_labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(true_labels, predictions, average='binary')
    return accuracy, precision, recall, f1, misclassified_samples

# 評価指標と誤分類されたサンプルの計算
accuracy, precision, recall, f1, misclassified_samples = evaluate(model, val_loader)
print(f'Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1 Score: {f1}')

# 誤分類されたサンプルを表示
print("\n誤分類されたサンプル:")
for sample in misclassified_samples:
    print(f'Text: {sample[0]}, True Label: {sample[1]}, Predicted Label: {sample[2]}')

