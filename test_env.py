"""test_env.py
Sandbox for testing pattern matching
3.7.22
"""

def main(fson):
    match fson:
        case { 
            "country": "US",
            "state": "OR", 
            "city": _
            }:
            print("city is in oregon")
        case {
            "city": _,
            "country": "US",
            "state": "WA"
            }:
            print("City is in washington")

if __name__ == "__main__":
    fake_json = {
        "country": "US",
        "state": "WA",
        "city": "Issaquah"
    }
    main(fake_json)