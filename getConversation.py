import requests
import os
import json
import time
from pymongo import MongoClient

dbName = "./setting.db"

# Mongo関係
# 接続先
hostName = "localhost"

# ポート番号(デフォルト27017)
port = 27017

# db名称
m_dbName = "皮肉だよ_5"



# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMbTTQEAAAAAQFDtSh3lkw1KFnFpPwsCD8fQErk%3DITmT3yjQNKGxGuPidUowBPWr9L9kbRg6qW5dd1wWB82cZ6Pc8J"


def create_url(con_id, id):
    tweet_fields = "tweet.fields=author_id,in_reply_to_user_id,conversation_id,referenced_tweets"
    query = "query=conversation_id:{}".format(con_id)
    max_results = "max_results=100"
    until_id = "until_id:{}".format(id)
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}&{}&{}".format(query, max_results, tweet_fields, until_id)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    # result = []
    response_body = response.json() ##全部取得
    response_data = response_body['data'] ##'data'の中身だけ取得
    # result = extract_values_with_key(response_data, 'text')
    # result = collect_data_with_key(response_data, 'text')
    # num = id ##該当ツイートのID
    # while num < response_body['id']: ##該当ツイートより小さいIDのツイートだけを取得
    #     result = response_data['id']

    rate_limit = response.headers['x-rate-limit-remaining']
    print('Rate limit remaining: ' + rate_limit)
    rate_limit_remaining = int(response.headers['x-rate-limit-remaining'])
    if rate_limit_remaining == 0:
        reset_time = int(response.headers['x-rate-limit-reset'])
        sleep_duration = max(0, reset_time - time.time()) + 60
        print(f'API rate limit reached. Sleeping for {sleep_duration} seconds.')
        time.sleep(sleep_duration)

    # return result
    return response_data
    # return response.json()

# 特定のキーを持つ値を抽出する関数
def extract_values_with_key(data, key):
    values = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                values.append(v)
            elif isinstance(v, (dict, list)):
                values.extend(extract_values_with_key(v, key))
    elif isinstance(data, list):
        for item in data:
            values.extend(extract_values_with_key(item, key))
    return values

# 特定のキーを含むデータ全体を集める関数
def collect_data_with_key(data, target_key):
    new_data = {"data": []}
    for item in data["data"]:
        if target_key in item:
            new_data["data"].append(item)
    return new_data

def main():
    db_client = MongoClient(hostName, port)
    db_db = db_client[m_dbName]
    # db_col = db_db[collection]

    list = [
  1726213721650004388,
  1726457549405479402,
  1726453978958115024,
  1726462418157793585,
  1726365077761388820,
  1726242883513332044,
  1726207451329081824,
  1726418207827992668,
  1726395009363218713,
  1725720155727298891,
  1726079343150104996,
  1726036413928595632,
  1726305788036284505,
  1726258298985554222,
  1726257818922307976,
  1726232668915032230,
  1726001646357164157,
  1725899104478462140,
  1726207932365492264,
  1726189076213379307,
  1726192315990200331,
  1726182750347252048,
  1726174207711863246,
  1726149410021900521,
  1726089943926423677,
  1726060229237068096,
  1726025287958479049,
  1726032375908540457,
  1726086791969775780,
  1725779848512299305,
  1726080276638626092,
  1725833596366450972,
  1725809817095397492,
  1725856982165590403,
  1726067139583549524,
  1725880844735451301,
  1725880844735451301,
  1725424330719560060,
  1726050396693766653,
  1725652091941871966,
  1726034329703477305,
  1725756648726347789,
  1726020082130997412,
  1725835075848425472,
  1725774706069118977,
  1725878298071502964,
  1725764684572467542,
  1725823639361319412,
  1725542971242873048,
  1725848990451675272,
  1725849252566552902

  ]
    
    filename = "saved_number.txt"
    try:
        # ファイルから変数の値を読み込む
        with open(filename, "r") as file:
            num = int(file.read())
    except FileNotFoundError:
        # ファイルが存在しない場合、初期値を設定
        num = 10000000
    
    try:
        # for id in list:
        #     # collection名
        #     collection = "会話_{}".format(num)
        #     db_col = db_db[collection]
        #     url = create_url(id)
        #     json_response = connect_to_endpoint(url)
        #     db_col.insert_many(json_response)
        #     # print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))
        #     num += 1
        for row in list:
            con_id, id_value = row  # 二次元配列の各行から要素を取得
            # collection名
            collection = "会話_{}".format(num)
            db_col = db_db[collection]
            url = create_url(con_id, id_value)  # create_url()の引数を変更
            json_response = connect_to_endpoint(url)
            db_col.insert_many(json_response)
            # print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))
            num += 1

        # 計算結果をファイルに保存
        with open(filename, "w") as file:
            file.write(str(num))
    except Exception as e:
        # エラーが発生した場合、前回の値を使用する
        print(f"エラーが発生しました: {e}")
        print(f"エラー会話idは {con_id} です")
        print("現在、会話", num-1, "まで取得済み")
        print("次、会話", num, "からスタート")
        with open(filename, "w") as file:
            file.write(str(num))

    print("現在、会話", num-1, "まで取得済み")
    print("次、会話", num, "からスタート")

if __name__ == "__main__":
    main()