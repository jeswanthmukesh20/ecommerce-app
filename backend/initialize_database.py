import requests
import random
import string
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-r",
    "--random-password",
    action=argparse.BooleanOptionalAction,
    default=False,
    help="Create Random string for password range from 6 - 20 characters."
)
parser.add_argument(
    "-p",
    "--password",
    type=str,
    default="password"
)
args = parser.parse_args()
characters = list(string.ascii_letters + string.digits + string.punctuation)
random.shuffle(characters)

API_KEY = "5vUvzHeZXQe05949yAk1Kg==MJAlA8P8w2PcqtPX"
api_url = 'https://api.api-ninjas.com/v1/randomuser'
register_url = "http://localhost:8000/register/manager"
login_url = "http://localhost:8000/login"
add_products = "http://localhost:8000/manage_product"

store_managers = []
for i in range(random.randint(2, 6)):
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        user = response.json()
        password = args.password if not args.random_password else "".join([random.choice(characters) for i in range(random.randint(6, 20))])
        user["password"] = password
        _ = requests.post(url=register_url, json={
            "username": user.get("username"),
            "email": user.get("email"),
            "password": user["password"]
        }).json()
        resp = requests.post(url=login_url, json={
            "username": user.get("username"),
            "password": user.get("password")
        }).json()
        user["access_token"] = resp["access_token"]
        store_managers.append(user)
    else:
        print("Error:", response.status_code, response.text)

if store_managers:
    with open("data.json", "r") as f:
        for data in json.load(f):
            user = random.choice(store_managers)
            headers = {
                "Authorization": f"Bearer {user['access_token']}"
            }
            data["images"] = ["no-picture.jpg" for i in range(10)]
            resp = requests.post(url=add_products, json=data, headers=headers).json()
            print(resp)

    with open("store_managers.json", "w") as f:
        json.dump(store_managers, f, indent=4)
