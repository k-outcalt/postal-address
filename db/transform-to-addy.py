"""transform-to-addy.py
Transforms a geojson into a json address to store in 
database

Note: because of difficulty with importing packages, 
each line is transformed into a string then back to a hash.
This is likely to impact performance greatly

Using insert_one instead of insert many
"""
import json
from socket import AddressInfo
import transform
import pymongo

RAW_ADDRESSES = 'sample_group.geojson'
MONGO_CONNECTION_STR = 'mongodb+srv://outcaltk-cluster:rjOBFu5GAKmsSGZ3@addresses.4q6sq.mongodb.net/addresses?retryWrites=true&w=majority'
ADDR_LIMIT = 1500

def populate_cluster(limit):
    # connect to MongoDB
    count = 0
    client = pymongo.MongoClient(MONGO_CONNECTION_STR)
    db = client.addressDB
    addrs = db.address

    # geojson => json => insert document
    with open(RAW_ADDRESSES) as file:
        for line in file:
            item = json.loads(line)
            addr = transform.create_hash_US_WA(item)
            addrs.insert_one(addr)

            count += 1
            if count >= limit:
                break


if __name__ == "__main__":
    populate_cluster(ADDR_LIMIT)

