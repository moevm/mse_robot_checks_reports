from pymongo import MongoClient

class DatabaseDAO:
    client = 0
    bd = 0
    collection = 0

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.verificated_docs
        self.collection = self.db.docs
