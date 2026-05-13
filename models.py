from pymongo import MongoClient
from app.config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_default_database()

# Collections
users_col = db["users"]
hospitals_col = db["hospitals"]
insurances_col = db["insurances"]
feedback_col = db["feedback"]
accidents_col = db["accidents"]
