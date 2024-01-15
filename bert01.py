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
MAX_LEN = 256
BATCH_SIZE = 8
EPOCHS = 3

# トークナイザーとモデルの初期化
tokenizer = BertTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-v3')
model = BertForSequenceClassification.from_pretrained('cl-tohoku/bert-base-japanese-v3')


# データセットの準備
# CSVファイルを読み込む
pos_data = pd.read_csv('/home/ishi0826/Templates/graduation-research/pst.csv')
neg_data = pd.read_csv('/home/ishi0826/Templates/graduation-research/ngt.csv')
test_data = pd.read_csv('/home/ishi0826/Templates/graduation-research/test.csv')

# テキスト中の '\n' を改行文字に置換
pos_data['text'] = pos_data['text'].replace(r'\\n', '\n', regex=True)
neg_data['text'] = neg_data['text'].replace(r'\\n', '\n', regex=True)
test_data['text'] = test_data['text'].replace(r'\\n', '\n', regex=True)

data = pd.concat([pos_data, neg_data])

# 訓練データセットとバリデーションデータセットに分割
train_data, val_data = train_test_split(data, test_size=0.2)
train_data = train_data.reset_index(drop=True)  # インデックスをリセット
val_data = val_data.reset_index(drop=True)      # インデックスをリセット

# データセットの準備
train_dataset = TextDataset(train_data, tokenizer, MAX_LEN)
val_dataset = TextDataset(val_data, tokenizer, MAX_LEN)
test_dataset = TextDataset(test_data, tokenizer, MAX_LEN)

# データローダーの設定
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=True)

# オプティマイザーの設定
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)

# 訓練ループ
for epoch in range(EPOCHS):
    model.train()
    total_train_loss = 0

    for batch in train_loader:
        optimizer.zero_grad()
        input_ids = batch['input_ids']
        attention_mask = batch['attention_mask']
        labels = batch['labels']
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        
        loss = outputs.loss
        total_train_loss += loss.item()
        loss.backward()
        optimizer.step()

    # 平均訓練ロスを計算
    avg_train_loss = total_train_loss / len(train_loader)

    # 検証フェーズ
    model.eval()
    total_val_loss = 0
    predictions, true_labels = [], []

    with torch.no_grad():
        for batch in val_loader:
            input_ids = batch['input_ids']
            attention_mask = batch['attention_mask']
            labels = batch['labels']

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss
            total_val_loss += loss.item()

            logits = outputs.logits
            batch_predictions = torch.argmax(logits, dim=1).tolist()
            predictions.extend(batch_predictions)
            true_labels.extend(labels.tolist())

    # 平均検証ロスを計算
    avg_val_loss = total_val_loss / len(val_loader)

    # 評価指標を計算
    accuracy = accuracy_score(true_labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(true_labels, predictions, average='binary')

    # 結果を表示
    print(f'Epoch {epoch + 1}/{EPOCHS}')
    print(f'Training Loss: {avg_train_loss:.3f}')
    print(f'Validation Loss: {avg_val_loss:.3f}')
    print(f'Accuracy: {accuracy:.3f}, Precision: {precision:.3f}, Recall: {recall:.3f}, F1 Score: {f1:.3f}')
    print('---------------------------')

    # テストフェーズ
def evaluate_test(model, data_loader):
    model.eval()
    predictions, true_labels = [], []

    with torch.no_grad():
        for batch in data_loader:
            input_ids = batch['input_ids']
            attention_mask = batch['attention_mask']
            labels = batch['labels']

            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            batch_predictions = torch.argmax(logits, dim=1).tolist()
            predictions.extend(batch_predictions)
            true_labels.extend(labels.tolist())

    accuracy = accuracy_score(true_labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(true_labels, predictions, average='binary')
    return accuracy, precision, recall, f1

# モデルをテストデータセットで評価
test_accuracy, test_precision, test_recall, test_f1 = evaluate_test(model, test_loader)
print(f'Test - Accuracy: {test_accuracy:.3f}, Precision: {test_precision:.3f}, Recall: {test_recall:.3f}, F1 Score: {test_f1:.3f}')