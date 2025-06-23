from pymongo import MongoClient

class DBEngine:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="deleitate_dev"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def create_client(self):
        return self.client

    def create_collection(self, collection_name):
        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)
        return self.db[collection_name]

    def insert_one(self, collection_name, document):
        collection = self.db[collection_name]
        return collection.insert_one(document)
