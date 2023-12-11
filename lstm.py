import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import MeCab
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

# Mecabの初期化
mecab = MeCab.Tagger("-Owakati -d /path/to/your/mecab-ipadic-neologd")

# カスタムトークナイザーの定義
def tokenize_with_mecab(text):
    return mecab.parse(text).split()

# データセットクラスの定義
class CustomDataset(Dataset):
    def __init__(self, dataframe, transform=None):
        self.data = dataframe
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        question_text = self.data.iloc[idx, 0]  # CSVの1列目を質問文として取得
        answer_text = self.data.iloc[idx, 1]    # CSVの2列目を回答文として取得
        label = self.data.iloc[idx, 2]          # CSVの3列目をラベルとして取得

        if self.transform:
            question_text = self.transform(question_text)
            answer_text = self.transform(answer_text)

        return {'question_text': question_text, 'answer_text': answer_text, 'label': label}

# LSTMモデルの定義
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMModel, self).__init__()
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        embedded = self.embedding(x)
        lstm_out, _ = self.lstm(embedded)
        output = self.fc(lstm_out[-1, :, :])
        output = self.sigmoid(output)
        return output

# 前処理関数の定義
def preprocess(text):
    return [tokenize_with_mecab(text)]

# データの読み込み
df = pd.read_csv('your_dataset.csv')  # CSVファイルのパスを指定してください

# データの分割（例: 8割を訓練データ、2割をテストデータ）
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# データセットの作成
train_dataset = CustomDataset(train_df, transform=preprocess)
test_dataset = CustomDataset(test_df, transform=preprocess)

# ボキャブラリの作成
vectorizer = CountVectorizer()
vectorizer.fit(train_df.iloc[:, 0])

# モデル、損失関数、オプティマイザの定義
input_size = len(vectorizer.get_feature_names())
hidden_size = 100
output_size = 1
model = LSTMModel(input_size, hidden_size, output_size)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# トレーニング
num_epochs = 5
for epoch in range(num_epochs):
    for batch in DataLoader(train_dataset, batch_size=64, shuffle=True):
        text_batch = batch['text'][0]
        label_batch = torch.tensor(batch['label']).float()

        # テキストをBoW形式に変換
        bow_batch = torch.tensor(vectorizer.transform(text_batch).toarray()).float()

        optimizer.zero_grad()
        output = model(bow_batch)
        loss = criterion(output, label_batch)
        loss.backward()
        optimizer.step()

    # テストデータで評価
    with torch.no_grad():
        predictions = []
        true_labels = []
        for batch in DataLoader(test_dataset, batch_size=64, shuffle=False):
            text_batch = batch['text'][0]
            label_batch = batch['label']

            # テキストをBoW形式に変換
            bow_batch = torch.tensor(vectorizer.transform(text_batch).toarray()).float()

            output = model(bow_batch)
            predictions.extend(output.round().squeeze().tolist())
            true_labels.extend(label_batch.tolist())

    accuracy = accuracy_score(true_labels, predictions)
    print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item():.4f}, Accuracy: {accuracy:.4f}')
