"""transform-address.py
module for transforming the raw data into hashes for
team's NoSQL collection
"""
import random 

ID = '_id'
COUNTRY = 'country'
TERRITORY = 'territory'
CITY = 'city'
POSTCODE = 'postcode'
STREET = 'street'
UNIT = 'unit'
NO = 'number' 

PROP = 'properties'

# postal code lists
CA_LIST = ['V6L', 'V5R', 'V6H', 'V6G', 'V6E', 'V6C', 'V6B', 'V6A', 'V5Z', 'V5Y']
BR_LIST = ['20010-000', '20010-010', '20010-030', '22775-005', '2775-009']

# TODO: Create hash for every required country-Kat
# Germany, India, Japan, North and South Korea, Mexico, Spain, UK, USA

def get_random_postcode_list(code_list, seed=None):
    random.seed(seed)
    return random.choice(code_list)

def get_random_postcode(digits=5, start=10_000, stop=99_999, seed=None):
    """generates random postcode with starting/stopping digits
    returns string
    """
    random.seed(seed)
    match digits:
        case 2:
            return str(random.randint(10, 99))
        case 3:
            return str(random.randint(100, 999))
        case 4:
            return str(random.randint(1_000, 9_999))
        case 5:
            return str(random.randint(10_000, 99_999))
        case _:
            return str(random.randint(start, stop))
    

def create_hash_US_WA(gj):
    """
    >>> create_hash_US_WA({"type":"Feature","properties":{"hash":"a61bdd50a9646a04","number":"119","street":"NW  41ST ST","unit":"","city":"SEATTLE","district":"KING","region":"","postcode":"98107","id":"324731.0"},"geometry":{"type":"Point","coordinates":[-122.3580529,47.6561133]}})
    {'_id': 'a61bdd50a9646a04', 'country': 'US', 'territory': 'WA', 'city': 'SEATTLE', 'postcode': '98107', 'street': 'NW  41ST ST', 'unit': '', 'number': '119'}
    """
    return {
        ID: gj[PROP]["hash"],
        COUNTRY: "US",
        TERRITORY: "WA",
        CITY: gj[PROP]["city"],
        POSTCODE: gj[PROP]["postcode"],
        STREET: gj[PROP]["street"],
        UNIT: gj[PROP]["unit"],
        NO: gj[PROP]["number"]
    }

def create_hash_BR_RJ(gj):
    """
    >>> create_hash_BR_RJ({"type":"Feature","properties":{"id":"","unit":"","number":"35","street":"Rua Represa dos Ciganos","city":"","district":"","region":"","postcode":"","hash":"3f6437097cdb6d24"},"geometry":{"type":"Point","coordinates":[-43.3457266,-22.9563213]}})
    {'_id': '3f6437097cdb6d24', 'country': 'BR', 'territory': 'RJ', 'city': 'Rio De Janeiro', 'postcode': '2775-009', 'street': 'Rua Represa dos Ciganos', 'unit': '', 'number': '35'}
    """
    try:
        sd = int(gj[PROP]["number"])
    except ValueError:
        sd = None
    return {
        ID: gj[PROP]["hash"],
        COUNTRY: "BR",
        TERRITORY: "RJ",
        CITY: "Rio De Janeiro",
        POSTCODE: get_random_postcode_list(BR_LIST, sd),
        STREET: gj[PROP]["street"],
        UNIT: gj[PROP]["unit"],
        NO: gj[PROP]["number"]
    }

def create_hash_CA_BC(gj):
    """
    >>> create_hash_CA_BC({"type":"Feature","properties":{"hash":"a74d51c1ce960f8b","number":"1816","street":"FRANCES ST","unit":"","city":"","district":"","region":"","postcode":"","id":""},"geometry":{"type":"Point","coordinates":[-123.0676717,49.2790801]}})
    {'_id': 'a74d51c1ce960f8b', 'country': 'CA', 'territory': 'BC', 'city': 'Vancouver', 'postcode': 'V6E', 'street': 'FRANCES ST', 'unit': '', 'number': '1816'}
    """
    try:
        sd = int(gj[PROP]["number"])
    except ValueError:
        sd = None
    return {
        ID: gj[PROP]["hash"],
        COUNTRY: "CA",
        TERRITORY: "BC",
        CITY: "Vancouver",
        POSTCODE: get_random_postcode_list(CA_LIST, sd),
        STREET: gj[PROP]["street"],
        UNIT: gj[PROP]["unit"],
        NO: gj[PROP]["number"]
    }
