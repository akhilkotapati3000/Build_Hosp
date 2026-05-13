import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY','supersecretkey')
    MONGO_URI = os.getenv('MONGO_URI','mongodb://127.0.0.1:27017/mark42')
    PORT = int(os.getenv('PORT',5000))
    DEBUG = os.getenv('DEBUG','true').lower() == 'true'
