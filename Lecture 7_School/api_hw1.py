import requests

url = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data["value"])
    else:
        print("Unable to load data, error code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")