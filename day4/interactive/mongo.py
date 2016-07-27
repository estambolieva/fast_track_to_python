from pymongo import MongoClient

# we run mongo on our local machine atm
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
# we specify the name of the databasse in mongo
DBS_NAME = 'donorschooce'
# the name of the collection in the database in mongo
COLLECTION_NAME = 'projects'
# selected 5 fields from 42 of each document in the collection
FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True,
          'total_donations': True, '_id': False}

# start the database collection
connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
# get the collection projects from database donorschooce
collection = connection[DBS_NAME][COLLECTION_NAME]
# get all documents contained within the collection while selecting only 5 of their fields
projects = collection.find(projection=FIELDS)

# print the first 10 documents
cnt = 0
for project in projects:
    print project
    cnt += 1
    if cnt == 11:
        break