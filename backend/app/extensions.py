from flask_pymongo import PyMongo
from pymongo import MongoClient

# Setup MongoDB here


MONGO_URL = "mongodb+srv://kalpanaranjan03:1234@techstaxcluster.rn5s3.mongodb.net/?retryWrites=true&w=majority&appName=techstaxCluster"
DB_NAME = "github_db"

def get_database():
    client = MongoClient(MONGO_URL)
    return client[DB_NAME]
