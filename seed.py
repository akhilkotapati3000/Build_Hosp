# Seed script: optional for real MongoDB
try:
    from pymongo import MongoClient
except Exception:
    print('pymongo not installed. To seed a real DB, install pymongo and re-run this script.')
    raise SystemExit(0)

import os
uri = os.getenv('MONGO_URI','mongodb://127.0.0.1:27017/mark42')
client = MongoClient(uri)
db = client.get_database()
db.users.delete_many({})
db.users.insert_one({'name':'Admin','email':'admin@buildhosp.com','password':'<hashed>','role':'admin'})
db.hospitals.delete_many({})
db.hospitals.insert_many([{'name':'Apollo Hospital','address':'Sector 21, Hyderabad','capacity':500,'available_beds':120,'contact':'+91 90000 12345'},{'name':'KIMS Hospital','address':'MG Road, Hyderabad','capacity':350,'available_beds':50,'contact':'+91 90000 54321'}])
print('Seeded MongoDB successfully.')
