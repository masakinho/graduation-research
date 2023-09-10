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
m_dbName = "TwitterDB3"



# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMbTTQEAAAAAQFDtSh3lkw1KFnFpPwsCD8fQErk%3DITmT3yjQNKGxGuPidUowBPWr9L9kbRg6qW5dd1wWB82cZ6Pc8J"


def create_url(con_id):
    tweet_fields = "tweet.fields=author_id,in_reply_to_user_id,conversation_id,referenced_tweets"
    query = "query=conversation_id:{}".format(con_id)
    max_results = "max_results=100"
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}&{}".format(query, max_results, tweet_fields)
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

    list = [1699000801375781318,
  1699002087215071584,
  1698896919828042137,
  1698992999768949110,
  1698619716754145460,
  1698974410450018745,
  1698936998122390006]
    
    filename = "saved_number.txt"
    try:
        # ファイルから変数の値を読み込む
        with open(filename, "r") as file:
            num = int(file.read())
    except FileNotFoundError:
        # ファイルが存在しない場合、初期値を設定
        num = 1000
    
    for id in list:
        # collection名
        collection = "会話_{}".format(num)
        db_col = db_db[collection]
        url = create_url(id)
        json_response = connect_to_endpoint(url)
        db_col.insert_many(json_response)
        # print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))
        num += 1

    # 計算結果をファイルに保存
    with open(filename, "w") as file:
        file.write(str(num))

    print("現在、会話", num-1, "まで取得済み")
    print("次、会話", num, "からスタート")

if __name__ == "__main__":
    main()