import requests

API_KEY = "e795e328b81cd7d7260e58c6fdebd6a0"

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_value = 8 * forecast_days
    filtered_data = filtered_data[:nr_value]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Tokyo"))
