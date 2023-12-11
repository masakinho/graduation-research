import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv('/home/ishi0826/Downloads/皮肉の文脈と発話文まとめ_皮肉です.csv')  # あなたのCSVファイルのパスを指定してください

# 改行文字を実際の改行に変換
df['text_column'] = df['text_column'].str.replace(r'\\n', '\n')

# 変換後のデータを確認
print(df.head())
