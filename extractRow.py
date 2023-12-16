import pandas as pd

def extract_columns(input_csv, output_csv, headers_to_extract):
    # CSVファイルを読み込む
    df = pd.read_csv(input_csv)

    # 指定したヘッダーの列だけを抜き取る
    extracted_columns = df[headers_to_extract]

    # 新しいCSVファイルに書き込む
    extracted_columns.to_csv(output_csv, index=False)

if __name__ == "__main__":
    # 入力CSVファイルのパス
    input_csv_path = "input.csv"

    # 出力CSVファイルのパス
    output_csv_path = "output.csv"

    # 抜き取りたいヘッダーの列のリスト
    headers_to_extract = ["Header1", "Header2", "Header3"]

    # 関数を呼び出してCSVファイルを生成
    extract_columns(input_csv_path, output_csv_path, headers_to_extract)

    print(f"CSVファイルが生成されました: {output_csv_path}")
