import azure.functions as func
import json
import logging
import pathlib

from addressSearch import searcher


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except Exception as e:
        return func.HttpResponse("Cannot get req_body: " + str(e), status_code=422)

    try:
        path = pathlib.Path(__file__).parent / 'addresses.json'
        f = open(path)
    except Exception as e:
        return func.HttpResponse("Cannot access database: " + str(e), status_code=503)

    try:
        data = json.load(f)
    except Exception as e:
        return func.HttpResponse("Cannot load database: " + str(e), status_code=503)

    if(req_body['mode'] == 'AddressSearch'):
        try:
            search_result = searcher.find_match_address(req_body, data)
        except Exception as e:
            return func.HttpResponse("Cannot search address: " + str(e), status_code=406)
    elif(req_body['mode'] == 'partialAddressSearch'):
        try:
            search_result = searcher.find_match_partial_address(req_body, data)
        except Exception as e:
            return func.HttpResponse("Cannot search partial address: " + str(e), status_code=406)  
    else:
        return func.HttpResponse("Invalid search mode", status_code=406)

    return func.HttpResponse(json.dumps(search_result, skipkeys = True, allow_nan = True, indent = 6), status_code=200)