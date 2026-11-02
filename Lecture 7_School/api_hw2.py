import requests

API_KEY = "api_key"
url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        weather_description = data["weather"][0]["description"]

        temperature = data["main"]["temp"]

        print(f"Weather in {city_name}: {weather_description}")
        print(f"Temperature: {temperature}°C")

    elif response.status_code == 404:
        print("Error: City not found. Please check the city name.")
    else:
        print(f"Failed to retrieve data, error code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")