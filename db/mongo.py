import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI not set in environment variables")

client = MongoClient(MONGO_URI)

# Optional: test connection
try:
    client.admin.command('ping')
    print("MongoDB connected successfully")
except Exception as e:
    print("MongoDB connection failed:", e)

db = client["resume_db"]
candidates_collection = db["candidates"]