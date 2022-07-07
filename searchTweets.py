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
m_dbName = "TwitterDB2"

# collection名
collection = "賢いね、な"

# 発行したBearer tokenを指定する
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMbTTQEAAAAAUnOkgE8XrmMO5%2FZPwlxkNW7%2F7Rk%3DJ7KEHxQqBl1BP55slTO2Tk3auu8d6S8I6SRSw0B9tPy7GVzEpu'

# Twitter APIのURL
search_url = "https://api.twitter.com/2/tweets/search/recent"

# 検索クエリ
query_params = {'query': '("かしこいね" OR "賢いね" OR "かしこいな" OR "賢いな")  -is:retweet -has:links -is:reply ',  'max_results': 100}

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
        result += response_body['data']
        
        rate_limit = response.headers['x-rate-limit-remaining']
        print('Rate limit remaining: ' + rate_limit)

        c = c + 1
        has_next = ('next_token' in response_body['meta'].keys() and c < 10)

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