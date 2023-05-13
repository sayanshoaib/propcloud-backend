from pymongo import MongoClient
from pymongo.collection import Database, Collection


USER_COLLECTION = "users"
PROPERTY_COLLECTION = "properties"
UNIT_COLLECTION = "units"
LOCATION_COLLECTION = "locations"


def db_conn() -> Database:
    client = MongoClient("mongodb://prop-cloud-db:27017/")
    db = client["propcloud_db"]
    return db


def get_collection(collection_name: str, db: Database) -> Collection:
    return db[collection_name]


def get_server_info() -> dict:
    client = MongoClient("mongodb://prop-cloud-db:27017/")
    db = client["propcloud_db"]
    server = db.client.server_info()
    return server
