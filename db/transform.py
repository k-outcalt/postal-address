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
DE_LIST = ['07545', '07552', '98527', '98529', '99084', '99099', '99423', '99427', '99894', '99898']
JP_LIST = ['104-0044', '104-0061', '104-0046', '104-6001', '103-0002']

# TODO: Create hash for every required country-Kat
# need to find: India, North Korea, UK

def get_seed(code):
    try:
        sd = int(code)
    except ValueError:
        sd = None
    return sd

def get_random_list_item(lst, seed=None):
    random.seed(seed)
    return random.choice(lst)

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
    sd = get_seed(gj[PROP]["number"])
    return {
        ID: gj[PROP]["hash"],
        COUNTRY: "BR",
        TERRITORY: "RJ",
        CITY: "Rio De Janeiro",
        POSTCODE: get_random_list_item(BR_LIST, sd),
        STREET: gj[PROP]["street"],
        UNIT: gj[PROP]["unit"],
        NO: gj[PROP]["number"]
    }

def create_hash_CA_BC(gj):
    """
    >>> create_hash_CA_BC({"type":"Feature","properties":{"hash":"a74d51c1ce960f8b","number":"1816","street":"FRANCES ST","unit":"","city":"","district":"","region":"","postcode":"","id":""},"geometry":{"type":"Point","coordinates":[-123.0676717,49.2790801]}})
    {'_id': 'a74d51c1ce960f8b', 'country': 'CA', 'territory': 'BC', 'city': 'Vancouver', 'postcode': 'V6E', 'street': 'FRANCES ST', 'unit': '', 'number': '1816'}
    """
    sd = get_seed(gj[PROP]["number"])
    return {
        ID: gj[PROP]["hash"],
        COUNTRY: "CA",
        TERRITORY: "BC",
        CITY: "Vancouver",
        POSTCODE: get_random_list_item(CA_LIST, sd),
        STREET: gj[PROP]["street"],
        UNIT: gj[PROP]["unit"],
        NO: gj[PROP]["number"]
    }

def create_hash_DE_TH(gj):
    """
    >>> create_hash_DE_TH({"type":"Feature","properties":{"hash":"53dd5298cc445e2f","number":"13","street":"Bei St. Bartholomäi","unit":"","city":"Schwarza","district":"","region":"","postcode":"","id":""},"geometry":{"type":"Point","coordinates":[10.5338576,50.6273767]}})
    {'_id': '53dd5298cc445e2f', 'country': 'DE', 'territory': 'TH', 'city': 'Schwarza', 'postcode': '99084', 'street': 'Bei St. Bartholomäi', 'unit': '', 'number': '13'}
    """
    sd = get_seed(gj[PROP]["number"])
    return {
        ID: gj[PROP]["hash"],
        COUNTRY: "DE",
        TERRITORY: "TH",
        CITY: gj[PROP]["city"],
        POSTCODE: get_random_list_item(DE_LIST, sd),
        STREET: gj[PROP]["street"],
        UNIT: gj[PROP]["unit"],
        NO: gj[PROP]["number"]
    }

def create_hash_JP_TK(gj):
    """
    >>> create_hash_JP_TK({"type":"Feature","properties":{"hash":"b391c71ea8d8bfc6","number":"5-9","street":"麹町六丁目","unit":"","city":"","district":"","region":"","postcode":"","id":""},"geometry":{"type":"Point","coordinates":[139.731181,35.6848]}})
    {'_id': 'b391c71ea8d8bfc6', 'country': 'JP', 'territory': 'TOKYO', 'city': 'Chuoku', 'postcode': '103-0002', 'street': '麹町六丁目', 'unit': '', 'number': '5-9'}
    """
    sd = get_seed(gj[PROP]["number"][0])
    return {
        ID: gj[PROP]["hash"],
        COUNTRY: "JP",
        TERRITORY: "TOKYO",
        CITY: "Chuoku",
        POSTCODE: get_random_list_item(JP_LIST, sd),
        STREET: gj[PROP]["street"],
        UNIT: gj[PROP]["unit"],
        NO: gj[PROP]["number"]
    }

def create_hash_MX_MX(gj):
    """
    >>> create_hash_MX_MX({"type":"Feature","properties":{"id":"","unit":"","number":"91","street":"NINGUNO","city":"IZTAPALAPA","district":"","region":"","postcode":"09040","hash":"dbbeb6d12a5b21ee"},"geometry":{"type":"Point","coordinates":[-99.0947565,19.3736838]}})
    {'_id': 'dbbeb6d12a5b21ee', 'country': 'MX', 'territory': 'CDMX', 'city': 'IZTAPALAPA', 'postcode': '09040', 'street': 'NINGUNO', 'unit': '', 'number': '91'}
    """
    return {
        ID: gj[PROP]["hash"],
        COUNTRY: "MX",
        TERRITORY: "CDMX",
        CITY: gj[PROP]["city"],
        POSTCODE: gj[PROP]["postcode"],
        STREET: gj[PROP]["street"],
        UNIT: gj[PROP]["unit"],
        NO: gj[PROP]["number"]
    }

def create_hash_ES_NC(gj):
    """
    >>> create_hash_ES_NC({"type":"Feature","properties":{"hash":"725dd5461d3a811e","number":"4","street":"CALLE CALLEJA","unit":"","city":"Abáigar","district":"Abáigar","region":"Navarra","postcode":"31280","id":"1"},"geometry":{"type":"Point","coordinates":[-2.1414442,42.6489724]}})
    {'_id': '725dd5461d3a811e', 'country': 'ES', 'territory': 'Navarra', 'city': 'Abáigar', 'postcode': '31280', 'street': 'CALLE CALLEJA', 'unit': '', 'number': '4'}
    """
    return {
        ID: gj[PROP]["hash"],
        COUNTRY: "ES",
        TERRITORY: gj[PROP]["region"],
        CITY: gj[PROP]["city"],
        POSTCODE: gj[PROP]["postcode"],
        STREET: gj[PROP]["street"],
        UNIT: gj[PROP]["unit"],
        NO: gj[PROP]["number"]
    }

def create_hash_KR_41(gj):
    """
    >>> create_hash_KR_41({"type":"Feature","properties":{"hash":"e3213c66e1b962dd","number":"31","street":"영동고속도로","unit":"","city":"수원시 장안구","district":"파장동","region":"경기도","postcode":"16201","id":"4111112900-63790"},"geometry":{"type":"Point","coordinates":[126.987395,37.3258245]}})
    {'_id': 'e3213c66e1b962dd', 'country': 'KR', 'territory': 'Gyeonggi', 'city': '수원시 장안구', 'postcode': '16201', 'street': '영동고속도로', 'unit': '', 'number': '31'}
    """
    return {
        ID: gj[PROP]["hash"],
        COUNTRY: "KR",
        TERRITORY: "Gyeonggi",
        CITY: gj[PROP]["city"],
        POSTCODE: gj[PROP]["postcode"],
        STREET: gj[PROP]["street"],
        UNIT: gj[PROP]["unit"],
        NO: gj[PROP]["number"]
    }