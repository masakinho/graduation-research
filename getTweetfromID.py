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
    url = create_url(1727560325049024841,
  1727571658016506190,
  1727559986203758929,
  1727533869304594596,
  1727443313425580051,
  1726986475802329193,
  1719543769144705442,
  1726966800959820114,
  1727513591644029294,
  1727486675641937950,
  1727500055391920290,
  1727498114704220276,
  1727219861124940036,
  1727479098686206349,
  1727448408255042028,
  1726837336753992175,
  1727267047783199064,
  1727454911091343725,
  1727454307791106228,
  1727267047783199064,
  1727391345973830100,
  1727356630411714764,
  1727374465053696234,
  1727361958968701362,
  1727361958968701362,
  1727318876193685947,
  1727243593792799132,
  1726241709468844446,
  1726996165839958397,
  1727276752853254271,
  1727178087782113665,
  1727272273659478114,
  1727238206478008333,
  1727225048971550839,
  1726856564777381964,
  1727192339939233795,
  1727143583243973074,
  1727140978908361053,
  1727152339289849880,
  1727123107444564099,
  1727100346017984665,
  1727084775452852289,
  1727124587450876256,
  1726768760751841432,
  1727078223241167139,
  1726560822229602403,
  1726959560769106180,
  1726979673270493346,
  1726971172297019829,
  1726966069095723372,
  1726886579057353176,
  1726892768008790355,
  1726955522501542226,
  1726854994564100532,
  1726936950035353684,
  1726881650632802435,
  1725717543732838789,
  1726941602864910438,
  1726921936566125005,
  1726888499763450082,
  1726763038358032601,
  1726889805622251822,
  1726542050517254423,
  1726896163109110225,
  1726822826743898257,
  1726851225398940023,
  1726864149249233043,
  1726838633733537908,
  1726812921911787964,
  1726823907309785391,
  1726800953712705938,
  1726767545209032763,
  1726610333786345899,
  1726405120987119822,
  1726435201952448749,
  1726728064305156593,
  1726001646357164157,
  1726344703308939499,
  1726450788967555209,
  1726615282419126782,
  1726605089702568378,
  1726248897562182078,
  1726449535134917034,
  1726592358509396010,
  1725394082875482474,
  1726577356889076035,
  1726580828367716502,
  1726516846160191530,
  1726581907255648639,
  1726571123062739390
  )
    json_response = connect_to_endpoint(url)
    # print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))
    db_client = MongoClient(hostName, port)
    db_db = db_client[m_dbName]
    db_col = db_db[collection]
    db_col.insert_many(json_response)

if __name__ == "__main__":
    main()