import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from typing import Any, List, Dict, Optional

load_dotenv()

class DBEngine:
    def __init__(self):
        self.uri: str = os.getenv("MONGO_URI_LOCAL", os.getenv("MONGO_URI", ""))
        self.db_name: str = os.getenv("MONGO_DB_NAME", "")

        if not self.uri:
            raise ValueError("No se encontró la URI de MongoDB (MONGO_URI_LOCAL o MONGO_URI) en el archivo .env")
        if not self.db_name:
            raise ValueError("No se definió el nombre de la base de datos (MONGO_DB_NAME) en el archivo .env")

        self.client: MongoClient = MongoClient(self.uri)
        self.db = self.client[self.db_name]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

    def insert_one(self, collection_name: str, data: Dict[str, Any]):
        return self.get_collection(collection_name).insert_one(data)

    def insert_many(self, collection_name: str, data_list: List[Dict[str, Any]]):
        return self.get_collection(collection_name).insert_many(data_list)

    def find_by_id(self, collection_name: str, doc_id: str) -> Optional[Dict[str, Any]]:
        return self.get_collection(collection_name).find_one({"_id": ObjectId(doc_id)})

    def find_all(self, collection_name: str, query: Dict[str, Any] = {}) -> List[Dict[str, Any]]:
        return list(self.get_collection(collection_name).find(query))

    def find_one(self, collection_name: str, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        return self.get_collection(collection_name).find_one(query)

    def update_by_id(self, collection_name: str, doc_id: str, update_data: Dict[str, Any]):
        return self.get_collection(collection_name).update_one(
            {"_id": ObjectId(doc_id)},
            {"$set": update_data}
        )

    def update_many(self, collection_name: str, query: Dict[str, Any], update_data: Dict[str, Any]):
        return self.get_collection(collection_name).update_many(
            query,
            {"$set": update_data}
        )

    def delete_by_id(self, collection_name: str, doc_id: str):
        return self.get_collection(collection_name).delete_one({"_id": ObjectId(doc_id)})

    def delete_many(self, collection_name: str, query: Dict[str, Any]):
        return self.get_collection(collection_name).delete_many(query)

    def count_documents(self, collection_name: str, query: Dict[str, Any] = {}) -> int:
        return self.get_collection(collection_name).count_documents(query)

    def list_collections(self) -> List[str]:
        return self.db.list_collection_names()
