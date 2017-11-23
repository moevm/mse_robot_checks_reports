from pymongo import MongoClient
import gridfs


client = MongoClient()
db = client.verificated_docs
collection = db.docs

print(collection.find())
print(collection.find().count())
for doc in collection.find():
    print(doc)