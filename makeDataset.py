import pandas as pd

def extract_and_accumulate(input_csv, output_csv):
    try:
        # 既存の出力CSVファイルを読み込み
        existing_df = pd.read_csv(output_csv)
    except FileNotFoundError:
        # 既存のファイルが存在しない場合は新しいDataFrameを作成
        existing_df = pd.DataFrame(columns=['conversation_id', 'text'])

    # 入力CSVファイルを読み込み
    df = pd.read_csv(input_csv)

    # 'conversation_id' と 'text' 列を抽出し、text中の「@」から始まり、次の空白までの文字列を削除
    df['text'] = df['text'].str.replace(r'@.*?\s', '', regex=True)

    # 'text' 中の「http」から始まり、次の空白までの文字列を削除
    df['text'] = df['text'].str.replace(r'http\S*\s?', '', regex=True)

    # 'id' 列を数値型に変換してから昇順にソート
    df['id'] = pd.to_numeric(df['id'], errors='coerce')
    df.sort_values(by='id', inplace=True)

    # 既存のDataFrameと新しいDataFrameを結合して蓄積
    accumulated_df = pd.concat([existing_df, df[['conversation_id', 'text']]], ignore_index=True)

    # 蓄積したDataFrameを出力CSVファイルとして保存
    accumulated_df.to_csv(output_csv, index=False)

# 固定の出力CSVファイルとして指定
output_csv_file = 'C:\\Users\\masakinho\\graduation-research\\neg_output.csv'

# 入力CSVファイルを変えながらデータを蓄積
extract_and_accumulate('C:\\Users\\masakinho\\Documents\\森研究室もろもろ\\修士論文\\会話2\\皮肉だよ.会話_374.csv', output_csv_file)

# 結果を表示
result_df = pd.read_csv(output_csv_file)
print(result_df)
