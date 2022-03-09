def find_match_address(req_body, json_database):

    search_result = []

    try:
        countries = req_body['searchCountries'].lower().strip().split(' ')
    except:
        return []

    if not(countries):
        return []

    for address in json_database:

        isValid = True

        if address['Country'].lower() not in countries:
            continue

        for key in req_body:
            try:
                if req_body[key] and address[key]:
                    if req_body[key].strip().lower() != address[key].strip().lower():
                        isValid = False
                        break
                elif req_body[key] and not address[key]:
                    isValid = False
                else:
                    continue
            except:
                continue

        if isValid:
            search_result.append(address)

    return search_result


def find_match_partial_address(req_body, json_database):

    search_result = []

    try:
        country = req_body['searchCountry'].lower().strip()
    except:
        return []

    if not(country):
        return []
    
    try:
        partial_address = req_body['partialAddress'].lower().strip().split(',')
    except:
        return []

    partial_address = list(map(lambda x: x.strip(), partial_address))

    for address in json_database:

        isValid = True

        if address['Country'].lower() != country:
            continue

        address_value = list(address.values())

        for i in range(len(address_value)):
            if address_value[i]:
                address_value[i] = address_value[i].lower()

        for i in partial_address:
            if i.lower() not in address_value:
                isValid = False
                break

        if isValid:
            search_result.append(address)

    return search_result