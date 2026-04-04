from pymongo import MongoClient
import os

MONGO_URI = "mongodb+srv://lakstark2104_db_user:Stark2104@cluster0.trnkmlw.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["resume_db"]

jobs_collection = db["jobs"]