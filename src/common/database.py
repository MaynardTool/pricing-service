import pymongo


class Database:
    # static variable, so every instances of Databse class can have this variable
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    # no init as we don't want any instances of Database to have this method unless you access it
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    # return a cursor object
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    # return all the elements
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)