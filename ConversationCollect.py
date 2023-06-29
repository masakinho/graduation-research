import tweepy
import json
import time
from pymongo import MongoClient
import re

# Twitter APIキー
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# MongoDB接続情報
mongodb_hostname = 'localhost'
mongodb_port = 27017
mongodb_database = 'TwitterDB2'
mongodb_collection = 'c_面白いな'

# Tweepyの認証
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# MongoDBクライアントの作成
client = MongoClient(mongodb_hostname, mongodb_port)
db = client[mongodb_database]
collection = db[mongodb_collection]

# 会話ツイートを収集してMongoDBに格納する関数
def collect_and_store_conversation_tweets(keyword):
    # キーワードを含むツイートを検索
    tweets = tweepy.Cursor(api.search, q=keyword, tweet_mode='extended').items()
    for tweet in tweets:
        if not hasattr(tweet, 'in_reply_to_status_id_str'):
            continue
        
        conversation = api.get_status(tweet.in_reply_to_status_id_str, tweet_mode='extended')
        
        # 先頭のツイートが全てのリンクを含まず、リツイートではない場合のみ処理を続ける
        if not contains_link(conversation.full_text) and not conversation.retweeted:
            conversation_text = conversation.full_text
            reply_text = remove_urls(tweet.full_text)
            
            # テキストが空でない場合のみ、MongoDBに格納
            if conversation_text.strip() != '' and reply_text.strip() != '':
                # ツイート情報を辞書形式に変換
                tweet_data = {
                    'tweet_text': conversation_text,
                    'reply_text': reply_text
                }
                
                # MongoDBに格納する前に、既に格納されていないか確認
                if collection.count_documents(tweet_data) == 0:
                    # MongoDBに格納
                    collection.insert_one(tweet_data)
            
            # APIアクセス制限の考慮
            remaining_calls = api.rate_limit_status()['resources']['search']['/search/tweets']['remaining']
            if remaining_calls == 0:
                reset_time = api.rate_limit_status()['resources']['search']['/search/tweets']['reset']
                sleep_duration = reset_time - int(time.time()) + 5  # 念のため余裕を持たせる
                print(f'API rate limit reached. Sleeping for {sleep_duration} seconds.')
                time.sleep(sleep_duration)

# URLを削除する関数
def remove_urls(text):
    return re.sub(r'http\S+|www\S+', '', text)

# ツイート内にリンクが含まれるかを判定する関数
def contains_link(text):
    return re.search(r'http\S+|www\S+', text) is not None

# キーワードを指定して会話ツイートを収集し、MongoDBに格納
collect_and_store_conversation_tweets('皮肉だよ')
