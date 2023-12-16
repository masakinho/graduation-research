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
m_dbName = "皮肉だよ_5"

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
    url = create_url(
      1734997721428414832,1734960459839930826,1735232258800529548,1735145299927330905,1734949095943627092,1734781475026014288,
      1734747036233474230,1734881172067688613,1734367025861103756,1734838626088006050,1734846476831133779,1734770441028563355,
      1734563079801942059,1734692756143177931,1734535567764054103,1734497277597880755,1734563079801942059,1734443458876846089,
      1734239005380857915,1733726959480537200,1734187812566778121,1734002430621479294,1734002430621479294,1733905109707608151,
      1733833597776511236,1732309247474692594,1733462667065762042,1733395546013122653,1729079279122801126,1732966192879681578,
      1733112892093006222
  )
    json_response = connect_to_endpoint(url)
    # print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))
    db_client = MongoClient(hostName, port)
    db_db = db_client[m_dbName]
    db_col = db_db[collection]
    db_col.insert_many(json_response)

if __name__ == "__main__":
    main()