""" 
import tweepy
import requests
import json
import time
from pymongo import MongoClient
import re

# Twitter APIキー
API_key = 'oXV2f7yThI2GKcd5GdvsbX2Sb'
API_secret = 'KYcyoH3FMXSksNCCrmeiglZgXCEw5A7PNjQpdBBnsNCQ1IVG3C'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMbTTQEAAAAAQFDtSh3lkw1KFnFpPwsCD8fQErk%3DITmT3yjQNKGxGuPidUowBPWr9L9kbRg6qW5dd1wWB82cZ6Pc8J'
Access_Token = '3391900333-hZOFgQJZAaBoPmLoD1xBpQU546dpkGzLT8QptKC'
Access_Token_Secret = 'aQtqrpxiClsHbQC3ymG1KyUvOUfVb1PhwIxmn5hE98woE'

# MongoDB接続情報
mongodb_hostname = 'localhost'
mongodb_port = 27017
mongodb_database = 'Conversation_sarcasm'
mongodb_collection = '皮肉だよ'

# Twitter APIのURL
search_url = "https://api.twitter.com/2/tweets/search/recent"

# 検索クエリ
query_params = {'query': '("皮肉です")  -is:retweet -has:links ',  'max_results': 100, 'tweet.fields': 'conversation_id'}

# Tweepyの認証
api = tweepy.Client(API_key, API_secret, bearer_token, Access_Token, Access_Token_Secret, wait_on_rate_limit=True)

# MongoDBクライアントの作成
client = MongoClient(mongodb_hostname, mongodb_port)
db = client[mongodb_database]
collection = db[mongodb_collection]

# 会話ツイートを収集してMongoDBに格納する関数
def collect_and_store_conversation_tweets(keyword):
    # キーワードを含むツイートを検索
    tweets = api.search_recent_tweets(query=keyword, tweet_fields='conversation_id', expansions='author_id', max_results=100)
    for tweet in tweets:
        if 'author_id' not in tweet:
            continue
        
        conversation = api.get_tweet(tweet.conversation_id, tweet_fields='author_id')
        
        # 先頭のツイートが全てのリンクを含まず、リツイートではない場合のみ処理を続ける
        if not contains_link(conversation.text) and not conversation.retweeted:
            conversation_text = conversation.text
            reply_text = remove_urls(tweet.text)
            
            # テキストが空でない場合のみ、MongoDBに格納
            if conversation_text.strip() != '' and reply_text.strip() != '':
                # ツイート情報を辞書形式に変換
                tweet_data = {
                    'tweet_text': conversation_text,
                    'reply_text': reply_text
                }
                
                # MongoDBに格納する前に、既に格納されていないか確認
                if not is_duplicate(tweet_data):
                    # MongoDBに格納
                    collection.insert_one(tweet_data)
            
            # APIアクセス制限の考慮
            if api.rate_limit_remaining() == 0:
                reset_time = api.rate_limit_reset() - time.time()
                sleep_duration = max(0, reset_time) + 5  # 念のため余裕を持たせる
                print(f'API rate limit reached. Sleeping for {sleep_duration} seconds.')
                time.sleep(sleep_duration)

# URLを削除する関数
def remove_urls(text):
    return re.sub(r'http\S+|www\S+', '', text)

# ツイート内にリンクが含まれるかを判定する関数
def contains_link(text):
    return re.search(r'http\S+|www\S+', text) is not None

# 既に格納されているかどうかを判定する関数
def is_duplicate(tweet_data):
    query = {'$and': [{'tweet_text': tweet_data['tweet_text']}, {'reply_text': tweet_data['reply_text']}] }
    return collection.count_documents(query) > 0

# キーワードを指定して会話ツイートを収集し、MongoDBに格納
collect_and_store_conversation_tweets('皮肉だよ')
 """

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
m_dbName = "TwitterDB2"

# collection名
collection = "お試しコレクション"

# 発行したBearer tokenを指定する
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMbTTQEAAAAAQFDtSh3lkw1KFnFpPwsCD8fQErk%3DITmT3yjQNKGxGuPidUowBPWr9L9kbRg6qW5dd1wWB82cZ6Pc8J'

# Twitter APIのURL
search_url = "https://api.twitter.com/2/tweets/search/recent"
# lookup_url = "https://api.twitter.com/2/tweets"

# 検索クエリ
query_params = {'query': '"皮肉です"  -が皮肉 -は皮肉 -の皮肉 -て皮肉 -いう皮肉 -も皮肉 -is:retweet -has:links ',
                'until_id': '1735278475181953170',
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
        response_data = response_body['data']
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