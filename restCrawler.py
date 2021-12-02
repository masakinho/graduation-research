#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
特定キーワードのツイート全部取得するスクリプト(REST)
--- 説明用サンプル ver ---
@author: yuhkan
"""

# sqlite3
import sqlite3

# Tweepy関係
import tweepy
from tweepy.errors import HTTPException

# MongoDB
from pymongo import MongoClient

### プログラム固有の関数、クラス ###
# 継続データを保存するDB
dbName = "./setting.db"

# サーチ文字列。記述方法はTwitterの/search/tweets に準ずる。
query = '"(皮肉)" OR "（皮肉）"'

# Consumer Key
CK = "Uq3SgVG7m9FzVmawtjtVRl059"

# Consumer Secret
CS = "3I5wnOG5wOtAW9yut2nGVqJk8BDNtV7z1mBmOS1zVD5SgUHPHP"

# Mongo関係
# 接続先
hostName = "localhost"

# ポート番号(デフォルト27017)
port = 27017

# db名称
m_dbName = "TwitterDB"

# collection名
collection = "Tweet_data"

### メインのプログラム ###
def main():

    # TwitterのApplication 限定認証(制限が緩い)
    auth1 = tweepy.AppAuthHandler(CK, CS)
    # リトライの実施、リトライ時のディレイ値、タイムアウト、リミットオーバーの自動処理を設定
    TwAPI = tweepy.API(auth = auth1, retry_count= 5,
                       retry_delay =3,timeout = 70, wait_on_rate_limit=True)

    # MongoDB 認証関係処理(格納先DBとCollectionの指定)
    # db_dst = MongoClient(hostName, port, username="test", password="test")[m_dbName][collection]
    db_client = MongoClient(hostName, port, username="test", password="test")
    exit()
    
    db_db = db_client.database_names()
    print(db_db)
    db_col = db_db.collection_names()
    # print()
    # db_dst.insert_one({"test":"text"})

    # sqlite3関連
    conn = sqlite3.connect(dbName)
    c = conn.cursor()

    # 変数の初期化
    # 今回の最初にとれたID=次回のsince_id
    next_max_id = 0

    # 取得ループの前回MIN値-1
    recent_max_id = 0

    # 取得するツイートの最古のID(=前回取得時の最新ID)を、テーブル"GeneralSettings"から得る
    since_id = 0
    q = 'SELECT MaxID FROM GeneralSettings LIMIT 1;'
    for row in c.execute(q):
        # 取得時に、「前回の最新」を含まないようにするため、IDはインクリメントする
        since_id = row[0] + 1

    # 初回の実行
    result = TwAPI.search_tweets(q=query, result_type="recent", count=100, 
                          since_id=since_id, include_entities=True)

    if len(result):
        # 初回が取得できた場合、そのIDを記録(次回起動時のsince_idとなる)
        next_max_id = result[0].id

    else:
        # 初回取得そのものが失敗した場合(カウントゼロ件など)
        conn.close()
        return -255

    exit()
    for tweet in result:
        a = tweet._json
        # print(a["text"])
        # データを格納実施。
        db_dst.insert_one(tweet._json)
    # IDの最小(=次回の最大)を記録
    recent_max_id = result[-1].id -1

    while len(result) != 0:

        # 想定ラストオーバー対策
        if(recent_max_id <= since_id):
            break

        try:
            result = TwAPI.search_tweets(q=query, result_type="recent", count=100,
                                  since_id=since_id, include_entities=True,
                                  max_id=recent_max_id)

            if(len(result) == 0):
                #取得したデータが無い=取得終了
                break

            for tweet in result:
                if(since_id >= tweet._json['id']):
                    break

                # データを格納実施。
                db_dst.insert_one(tweet._json)

            recent_max_id = result[-1].id -1

        except HTTPException as exc:
            #tweepエラー発生時は、実施を巻き戻してエラー終了する。
            db_dst.remove({'id' : { '$gt': since_id}})

            return -255
        except KeyboardInterrupt:
            # CTRL+C対応
            break

        except Exception as exc:
            # その他エラー全般は無視する
            pass

    if next_max_id != 0:
        # 次回の最終IDを記録
        q = 'UPDATE GeneralSettings SET MaxID = ' + str(next_max_id) + ';'
        c.execute(q)

        # コミット
        conn.commit()

    #終了前処理
    conn.close()
    return 0

if __name__ == '__main__':
    main()