from pymongo import MongoClient
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
        fs.put(file)
        self.collection.insert_one(skelet)



