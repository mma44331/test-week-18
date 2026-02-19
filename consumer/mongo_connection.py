import pymongo
def get_mongo_conn():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    my_db = client['mymongo']
    my_coll = my_db['warning']
    return my_coll