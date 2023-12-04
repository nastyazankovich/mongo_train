import pymongo

mongo_url = "mongodb://localhost:27017/"
client = pymongo.MongoClient(mongo_url)
# print(client.list_database_names())
database = client.mydb
# print(database.list_collection_names())
table = database.users
prod = database.products
for i in prod.find({"price": {"$lt": 900}}):
    print(i)
# for document in table.find().sort('_id', pymongo.DESCENDING):
#     print(document)

# table.delete_one({"name":'John'})

# table.update_one({"name": "Mike"}, {"$set": {"age": 40}})
# for document in table.find({"age": {"$gt": 30}}):
#     print(document)