import tweepy
import json
import time
from pymongo import MongoClient
import re

# Twitter APIキー
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMbTTQEAAAAA6P1vTv6%2Fv8C6jukgHu%2F3tjXC3%2FU%3DQgugmAazWmHiaTpZH3GbEoWQArxyReR7snc0Zn5oNIAQmYApuT'

# MongoDB接続情報
mongodb_hostname = 'localhost'
mongodb_port = 27017
mongodb_database = 'Conversation_sarcasm'
mongodb_collection = '皮肉だよ'

# Tweepyの認証
auth = tweepy.AppAuthHandler(bearer_token)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# MongoDBクライアントの作成
client = MongoClient(mongodb_hostname, mongodb_port)
db = client[mongodb_database]
collection = db[mongodb_collection]

# 会話ツイートを収集してMongoDBに格納する関数
def collect_and_store_conversation_tweets(keyword):
    # キーワードを含むツイートを検索
    tweets = api.search_all_tweets(query=keyword, tweet_fields='referenced_tweets', expansions='author_id', max_results=100)
    for tweet in tweets:
        if not hasattr(tweet, 'referenced_tweets'):
            continue
        
        conversation = api.get_tweet(tweet.referenced_tweets[0].id, tweet_fields='text,author_id')
        
        # 先頭のツイートが全てのリンクを含まず、リツイートではない場合のみ処理を続ける
        if not contains_link(conversation.text) and tweet.author_id != conversation.author_id:
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
                if collection.count_documents(tweet_data) == 0:
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

# キーワードを指定して会話ツイートを収集し、MongoDBに格納
collect_and_store_conversation_tweets('皮肉だよ')

