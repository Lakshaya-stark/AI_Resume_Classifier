from pymongo import MongoClient

MONGO_URI = "mongodb+srv://lakstark2104_db_user:GSOfKFtsTz11YeWv@cluster0.trnkmlw.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["resume_db"]


candidates_collection = db["candidates"]