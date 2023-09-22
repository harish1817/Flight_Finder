import requests
import os

USERNAME = os.getenv("c2fe5a212028ce922f60dbe1a11cc7cb/flightDeals")

PROJECT = "Flight Deals"
SHEET = "users"

base_url = "https://api.sheety.co"

def post_new_row(first_name, last_name, email):
    endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
    url = "https://api.sheety.co/c2fe5a212028ce922f60dbe1a11cc7cb/flightDeals/users"

    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=url, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)

