import pymongo
from pymongo import MongoClient


cluster = MongoClient(
    "mongodb+srv://shlomoitzjak:<password>@cluster0.lntqq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
db = cluster["test"]
collection = db["test"]

post = {"_id": 0, "name":"salomon", "score": 5}

collection.insert_one(post)