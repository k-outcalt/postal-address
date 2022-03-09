"""transform-address.py
module for transforming the raw data into hashes for
team's NoSQL collection
"""

ID = '_id'
COUNTRY = 'country'
TERRITORY = 'territory'
CITY = 'city'
POSTCODE = 'postcode'
STREET = 'street'
UNIT = 'unit'
NO = 'number' 

PROP = 'properties'

# TODO: Create hash for every required country-Kat
# Brazil, Canada, Germany, India, Japan, North and South Korea, Mexico, Spain, UK, USA

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
    {'_id': '3f6437097cdb6d24', 'country': 'BR', 'territory': 'RJ', 'city': 'Rio De Janeiro', 'postcode': '}
    """