
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://abdulwahabiddris08:pymongo-0552500930@cluster0.lihshse.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
db = client.myApp
users = db["users"]
comments = db["comments"]
