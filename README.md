# postal-address
## TODO
1. create cached country-specific address formats for required countries (can use regex for address validation)
2. test address validation for the required countries
3. download irl addresses or create fake ones
4. wrap this in a MongoDB collection
5. work on searching by address
    completely filled address
    partially filled address
6. UI
    * submitting a country to get the format
    * country-specific format
    * submitting an address to get a list of addresses

## requirements to run
* `Python 3.10.*` for Case/Switch feature
* `Flask 2.*` for server 
* Internet connection to use API
## how to run
1. clone repo
2. open terminal or command prompt
3. navigate to the directory postal-address
4. use this command: `export FLASK_APP=app.py`
5. `flask run`
6. open up in browser or Postman at \<http>://\<ip_address>:\<port>

