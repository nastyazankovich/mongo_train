import datetime
import pymongo

mongo_url = "mongodb://localhost:27017/"
client = pymongo.MongoClient(mongo_url)
# print(client.list_database_names())
database = client.article
# print(database.list_collection_names())
table = database.user
# print(table.count_documents({}))
# print(table.find_one())
# print(table.find().sort('_id', pymongo.DESCENDING))
# for document in table.find().sort('_id', pymongo.DESCENDING):
# print(document)
# user1 = {"_id": "qwertyui123456",
#          'username': 'samy_',
#          'name': 'Pasha',
#          'sex': 'M',
#          'address': 'Somewhere in Kipr',
#          'mail': 'pavel83@mail.com',
#          'birthdate': '14/02/1996'}
# post_id = table.insert_one(user1).inserted_id
# new_users = [{"name":"Mike",
#               "username":"latestpost",
#               "date":datetime.datetime(2009, 11, 12, 11, 14)},
#              {"name": "Eliot",
#               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
# final = table.insert_many(new_users)
# print(final.inserted_ids)
# print(table.find_one({"name":'Pasha'}))
# table.delete_one({"name":'Mike'})
# myquery = ({"name": {"$in": ['Mike', 'Eliot']}})
# x = table.delete_many(myquery)
# print(x.deleted_count, "documents deleted.")
mydb = client.testDB
mycoll = mydb.testColl
