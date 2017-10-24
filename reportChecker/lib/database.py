from pymongo import MongoClient
from bson import ObjectId
import gridfs

class DatabaseDAO:
    client = 0
    bd = 0
    collection = 0

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.verificated_docs
        self.collection = self.db.docs

    def saveDoc(self, name, discipline, file):
        skelet = {}
        skelet.update({"name":name})
        skelet.update({"discipline":discipline})

        fs = gridfs.GridFS(self.db, collection="arch")
        fileId = fs.put(file)
        skelet.update({"fileId":fileId})
        self.collection.insert_one(skelet)



