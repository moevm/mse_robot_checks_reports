#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson import ObjectId
import os
import gridfs
import codecs

class DatabaseDAO:
    client = 0
    bd = 0
    collection = 0

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.verificated_docs
        self.collection = self.db.docs

    def saveDoc(self, name, discipline, filename):
        skelet = {}
        skelet.update({"name":name})
        skelet.update({"discipline":discipline})
        
        fs = gridfs.GridFS(self.db, collection="arch")
        print("FILEPATH: " + filename)
        file = open(filename, "rb") #codecs #,encoding='utf-8', errors='strict'
        fileId = fs.put(file.read())
        skelet.update({"fileId":fileId})
        self.collection.insert_one(skelet)

# dbdao = DatabaseDAO()
# dbdao.saveDoc('vasya','litrball','/root/Documents/se_project/mse_robot_checks_reports/attachments/6303-ПРОГ-ИВАНОВ-ИВАН.zip')

# cclient = MongoClient()
# cdb = cclient.verificated_docs
# ccollection = cdb.docs

# print(ccollection.find())
# print(ccollection.find().count())
# for doc in ccollection.find():
#     print(doc)

