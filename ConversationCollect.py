import requests
import re
import time
import sys
from typing import Any
from pymongo import MongoClient

dbName = "./setting.db"

# Mongo関係
# 接続先
hostName = "localhost"

# ポート番号(デフォルト27017)
port = 27017

# db名称
m_dbName = "db名称"

# collection名
collection = "collection名"

# 発行したBearer tokenを指定する
bearer_token = 'bearer token'

# Twitter APIのURL
search_url = "https://api.twitter.com/2/tweets/search/recent"
# lookup_url = "https://api.twitter.com/2/tweets"

# 検索クエリ
query_params = {'query': '"キーワード" -is:retweet -has:links ',
                # 'until_id': '1735278475181953170',
                'max_results': 100, 'tweet.fields': 'conversation_id,in_reply_to_user_id,author_id'}


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

# def create_url(tweet_id):
#     tweet_fields = "tweet.fields=in_reply_to_user_id,conversation_id"
#     ids = "ids={}".format(tweet_id)
#     # You can adjust ids to include a single Tweets.
#     # Or you can add to up to 100 comma-separated IDs
#     url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
#     return url

def create_url_con(tweet_id):
    tweet_fields = "tweet.fields=in_reply_to_user_id,in_reply_to_tweet_id,conversation_id"
    ids = "query=conversation_id:{}".format(tweet_id)
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(ids, tweet_fields)
    return url

def connect_to_endpoint_recent(search_url, headers, params):
    has_next = True
    c = 0
    result: Any = []
    while has_next:
        response = requests.request("GET", search_url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        response_body = response.json()
        # response_data = response_body['data']
        # print(response_data)
        # result += response_body['data']
        

        response_con = collect_data_with_key(response_body, 'in_reply_to_user_id')
        print(response_con['data'])

        # JSONデータ内のテキストフィールドのUnicodeエスケープシーケンスを削除、'text'フィールドの処理
        # for item in response_con['data']:
        #     if 'text' in item:
        #         # item['text'] = remove_unicode_escape_sequences(item['text'])
        #         item['text'] = convert_quotes_and_escape(item['text'])

        result += response_con['data']

        rate_limit = response.headers['x-rate-limit-remaining']
        print('Rate limit remaining: ' + rate_limit)

        c = c + 1
        has_next = ('next_token' in response_body['meta'].keys() and c < 1)

        # next_tokenがある場合は検索クエリに追加
        if has_next:
            query_params['next_token'] = response_body['meta']['next_token']

        # rate_limit_remaining = int(response.headers['x-rate-limit-remaining'])
        # if rate_limit_remaining == 0:
        #     reset_time = int(response.headers['x-rate-limit-reset'])
        #     sleep_duration = max(0, reset_time - time.time()) + 60
        #     print(f'API rate limit reached. Sleeping for {sleep_duration} seconds.')
        #     time.sleep(sleep_duration)

    return result

def connect_to_endpoint_lookup(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    
    response_body = response.json()
    print(response.json())
    return response_body

def collect_data_with_key(data, target_key):
    new_data = {"data": []}
    for item in data["data"]:
        if target_key in item:
            new_data["data"].append(item)
    return new_data

# Unicodeエスケープシーケンスを削除する関数
# def remove_unicode_escape_sequences(input_str):
#     return input_str.encode('utf-8').decode('unicode_escape')

# シングルクォートをダブルクォートに変換し、ダブルクォートをエスケープする関数
def convert_quotes_and_escape(input_str):
    return input_str.replace("'", '"').replace('"', r'\"').replace('\n', '\\n')

def main():
    db_client = MongoClient(hostName, port)
    db_db = db_client[m_dbName]
    db_col = db_db[collection]

    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint_recent(search_url, headers, query_params)
    print(json_response)
    if isinstance(json_response, dict):
        print("my_dictは辞書型です。")
    else:
        print("my_dictは辞書型ではありません。")
        print(type(json_response))
        sys.exit()
    db_col.insert_many(json_response)

if __name__ == "__main__":
    main()