from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client["hello"]
collation= db["아프간"]
newlike = collation.find()
t = 0
for i in newlike:
    t = t +  int(i.get("like"))
print(t)