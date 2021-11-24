import pymongo
# import dnspython
myclient = pymongo.MongoClient("")

mydb = myclient["mydatabase"]
print(myclient.list_database_names())
