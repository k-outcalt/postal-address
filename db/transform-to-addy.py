"""transform-to-addy.py
Transforms a geojson into a json address that we can store in
out database

Note: because of difficulty with importing packages, 
each line is transformed into a string then back to a hash.
This is likely to impact performance greatly
"""
import json
import transform

RAW_ADDRESSES = 'sample_group.geojson'

def main(count):
    with open(RAW_ADDRESSES) as file:
        
        for line in file:
            item = json.loads(line)
            print(transform.create_hash_US_WA(item))
            count -= 1
            print("count is: ", count)
            if count < 1:
                break

if __name__ == "__main__":
    main(10)

