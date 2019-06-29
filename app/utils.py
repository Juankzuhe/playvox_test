import pymongo
from django.db.utils import ConnectionDoesNotExist


def setup_cursor():
    try:
        client = pymongo.MongoClient('mongodb://mongodb:27017/')

        db = client
        return db
    except ConnectionDoesNotExist:
        return None
