import requests
import os
import json
from pymongo import MongoClient

dbName = "./setting.db"

# Mongo関係
# 接続先
hostName = "localhost"

# ポート番号(デフォルト27017)
port = 27017

# db名称
m_dbName = "皮肉です_3"

# collection名
collection = "元ツイート集"

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMbTTQEAAAAAQFDtSh3lkw1KFnFpPwsCD8fQErk%3DITmT3yjQNKGxGuPidUowBPWr9L9kbRg6qW5dd1wWB82cZ6Pc8J"


def create_url(*ids):
    if len(ids) < 1 or len(ids) > 100:
        raise ValueError("You must provide between 1 and 100 IDs.")
    
    tweet_fields = "tweet.fields=author_id,conversation_id"
    ids_str = ",".join(map(str, ids))
    url = "https://api.twitter.com/2/tweets?ids={}&{}".format(ids_str, tweet_fields)
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
    response_body = response.json()
    return response_body['data']


def main():
    url = create_url(1723929116884255141,
  1723914083823710583,
  1723872307007868954,
  1723786470555836679,
  1723750182695928113,
  1723502626602647973,
  1723663487841530008,
  1723635113278464267,
  1723541606274601075,
  1723519319290830922,
  1723290504278991337,
  1723284778215260428,
  1723194605812990020,
  1723188104369225749,
  1722918267306832085,
  1721796265254817925,
  1722381286692757811,
  1722929010890719742,
  1722832113068896643,
  1722482221800685774)
    json_response = connect_to_endpoint(url)
    # print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))
    db_client = MongoClient(hostName, port)
    db_db = db_client[m_dbName]
    db_col = db_db[collection]
    db_col.insert_many(json_response)

if __name__ == "__main__":
    main()