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

RAW_ADDRESSES = 'kr_41_provincewide-addresses-state.geojson'
MONGO_CONNECTION_STR = ''
ADDR_LIMIT = 1500

def test_hash(limit=10):
    count = 0
    with open(RAW_ADDRESSES) as file:
        for line in file:
            item = json.loads(line)
            #print(item)

            addr = transform.create_hash_KR_41(item)
            
            print(addr)
            count += 1
            if count >= limit:
                break


def populate_cluster(limit):
    # connect to MongoDB
    client = pymongo.MongoClient(MONGO_CONNECTION_STR)
    db = client.addressDB
    addrs = db.address

    # geojson => json => insert document
    count = 0
    with open(RAW_ADDRESSES) as file:
        for line in file:
            item = json.loads(line)
            addr = transform.create_hash_KR_41(item)
            try:
                addrs.insert_one(addr)
                count += 1
            except pymongo.errors.DuplicateKeyError:
                continue

            if count % 100 == 0:
                print("100 addresses recorded, total: ", count)
            if count >= limit:
                break


if __name__ == "__main__":
    populate_cluster(ADDR_LIMIT)
    # test_hash(10)

