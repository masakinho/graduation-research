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
m_dbName = "皮肉です_5"

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
      1737254036796215563, 1736732030816440412, 1737126138600652902, 1737276946038579542, 1737272539720843573, 1736688158497218936, 1737074247707840545, 1736741019511898382, 1736741019511898382, 1737176779100729789, 1736720273729274274, 1736243572767432938, 1737105400472989783, 1737086716677443963, 1737082236254683543, 1736812704919433310, 1736710674573820164, 1736953427308237090, 1736012659584278760, 1736682131693490471, 1736179628962943237, 1736901953219965130, 1736651009043378476, 1736699775167422900, 1736795041858039991, 1736699686021722142, 1736893036087689388, 1735798394038428149, 1736788638065897845, 1736662003325055164, 1736355605173129361, 1736879939990044977, 1736730177252839576, 1736726279586722189, 1733053769716547596, 1736513634648690790, 1736606178036359641, 1736664578338255321, 1736637641830109222, 1736189105841811543, 1736631233684340877, 1736662574601744630, 1735248168437367065, 1736532884910190938, 1736624603781640445, 1734793577325346822, 1736369663490318339, 1736582628793524426, 1736353564853969339, 1736591312797991231, 1736513550238257378, 1736366060646129728, 1736368824696569880, 1736215618964406582, 1736274990054695294, 1736218956430823570, 1736361078328840441, 1736200305061380482  )
    json_response = connect_to_endpoint(url)
    # print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))
    db_client = MongoClient(hostName, port)
    db_db = db_client[m_dbName]
    db_col = db_db[collection]
    db_col.insert_many(json_response)

if __name__ == "__main__":
    main()