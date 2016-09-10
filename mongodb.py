from pymongo import MongoClient
import string

client=MongoClient()
db=client.irectotyperdb

collection=db['20150721']
#collection=db.Collections

print(db.collection_names()) 
print(collection.count())
#query=db.collection.20150721
#print(query.count())