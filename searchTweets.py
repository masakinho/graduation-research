import requests
import re
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
bearer_token = 'Bearer token'

# Twitter APIのURL
search_url = "https://api.twitter.com/2/tweets/search/recent"

# 検索クエリ
query_params = {'query': '("keyword")  -is:retweet -has:links ',  'max_results': 100, 'tweet.fields': 'conversation_id'}

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(search_url, headers, params):
    has_next = True
    c = 0
    result = []
    while has_next:
        response = requests.request("GET", search_url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        response_body = response.json()
        print(response_body)
        print(response_body['data'])
        result += response_body['data']
        
        rate_limit = response.headers['x-rate-limit-remaining']
        print('Rate limit remaining: ' + rate_limit)

        c = c + 1
        has_next = ('next_token' in response_body['meta'].keys() and c < 1)

        # next_tokenがある場合は検索クエリに追加
        if has_next:
            query_params['next_token'] = response_body['meta']['next_token']

    return result

def main():
    db_client = MongoClient(hostName, port)
    db_db = db_client[m_dbName]
    db_col = db_db[collection]

    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)
    # print(json_response)
    db_col.insert_many(json_response)

if __name__ == "__main__":
    main()