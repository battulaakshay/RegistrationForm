from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://bathulaakshay01:Akshay2001@cluster0.qlrfsq9.mongodb.net/?retryWrites=true&w=majority")


db = client.tood_db

collection_name = db["todo_collection"]
