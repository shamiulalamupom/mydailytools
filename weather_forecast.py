import requests
from functools import lru_cache

@lru_cache(maxsize=None)
def display_weather():
    cities = ["Paris", "London", "Tokyo", "Montpellier", "Lyon"]

    print("Select the name of the city which you want to see the forecast of: ")
    for city in cities:
        print(city)

    inp = input("Now enter the name of the city: ")

    url = f"http://api.weatherapi.com/v1/forecast.json?key=7415433cc163485cb8d93117242204&q={inp}&days=7&aqi=yes&alerts=no"
    response = requests.get(url)
    json = response.json()

    forecasts = [{"date": day["date"], "data": [{"max_temp": day["day"]["maxtemp_c"], "min_temp": day["day"]["mintemp_c"], "weather": day["day"]["condition"]["text"], "humidity": day["day"]["avghumidity"], "wind": day["day"]["avgvis_km"]}]} for day in json["forecast"]["forecastday"]]

    for forecast in forecasts:
        print(f"{forecast['date']}")
        for data in forecast["data"]:
            print(f"\tMinimum Temperature: {data['min_temp']}°C\n\tMaximum Temperature: {data['max_temp']}°C\n\tWeather: {data['weather']}\n\tHumidity: {data['humidity']}%\n\tWind: {data['wind']} km/h")

if __name__ == "__main__":
    display_weather()

