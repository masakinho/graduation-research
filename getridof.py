from pymongo import MongoClient

dbName = "./setting.db"

# Mongo関係
# 接続先
hostName = "localhost"

# ポート番号(デフォルト27017)
port = 27017

# db名称
m_dbName = "TwitterDB2"

db_client = MongoClient(hostName, port)
old_db = db_client["TwitterDB3"]  # 古いデータベースの名前に合わせて変更
new_db = db_client["TwitterDB4"]  # 新しいデータベースの名前に合わせて変更

# 取り除く言葉
word_to_remove = "http"

# キー
key_to_search = "text"

# 古いデータベースから特定の条件を持つドキュメントを取得
old_collection = old_db["元ツイート集"]  # コレクションの名前に合わせて変更
documents = old_collection.find({key_to_search: {"$regex": word_to_remove, "$options": "i"}})

# 特定の言葉を含まないドキュメントを新しいデータベースに挿入
new_collection = new_db["リンクを除いた元ツイート集"]  # 新しいコレクションの名前に合わせて変更
for document in documents:
    if key_to_search in document and word_to_remove not in document[key_to_search]:
        new_collection.insert_one(document)

# MongoDB接続を閉じる
db_client.close()

