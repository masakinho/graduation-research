import pandas as pd
import MeCab

# MeCabの初期化
mecab = MeCab.Tagger("-Owakati -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")

# カスタムトークナイザーの定義
def tokenize_with_mecab(text):
    return mecab.parse(text).split()

# CSVファイルの読み込み
df = pd.read_csv('/home/ishi0826/Downloads/皮肉の文脈と発話文まとめ_皮肉です.csv')  # 実際のファイルパスを指定してください

# 改行文字を実際の改行に変換
df['Context'] = df['Context'].str.replace(r'\n', ' ')
df['Utterance'] = df['Utterance'].str.replace(r'\n', ' ')

# 単語分割を実施
df['Context'] = df['Context'].apply(tokenize_with_mecab)
df['Utterance'] = df['Utterance'].apply(tokenize_with_mecab)

# 変換後のデータを確認
print(df)

