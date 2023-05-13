from pymongo import MongoClient
from pymongo.collection import Collection


def db_conn(collection_name: str) -> Collection:
    client = MongoClient("mongodb://prop-cloud-db:27017/")
    db = client["propcloud_db"]
    collection = db[collection_name]
    return collection


def get_server_info() -> dict:
    client = MongoClient("mongodb://prop-cloud-db:27017/")
    db = client["propcloud_db"]
    server = db.client.server_info()
    return server
