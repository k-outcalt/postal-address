import json
import requests

url = 'https://address-search.azurewebsites.net/api/addresssearch'

myobj = {
"mode": "AddressSearch",
"searchCountries": "usa japan canada india",
"First Name": "Jesse"
}

data = json.dumps(myobj)

for i in range(500):
    x = requests.post(url, data = data)
    print(x.text)
    print(i)