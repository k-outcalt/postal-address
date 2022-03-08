"""transform-address.py
module for transforming the raw data into hashes for
team's NoSQL collection
"""

# TODO: Create hash for every required country-Kat

def create_hash_US_WA(gj):
    """
    >>> create_hash_US_WA({"type":"Feature","properties":{"hash":"a61bdd50a9646a04","number":"119","street":"NW  41ST ST","unit":"","city":"SEATTLE","district":"KING","region":"","postcode":"98107","id":"324731.0"},"geometry":{"type":"Point","coordinates":[-122.3580529,47.6561133]}})
    {'_id': 'a61bdd50a9646a04', 'country': 'US', 'territory': 'WA', 'city': 'SEATTLE', 'postcode': '98107', 'street': 'NW  41ST ST', 'unit': '', 'number': '119'}
    """
    new_hash = {
        "_id": gj["properties"]["hash"],
        "country": "US",
        "territory": "WA",
        "city": gj["properties"]["city"],
        "postcode": gj["properties"]["postcode"],
        "street": gj["properties"]["street"],
        "unit": gj["properties"]["unit"],
        "number": gj["properties"]["number"]
    }
    return new_hash