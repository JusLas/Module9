import requests


def get_data():

    response = requests.get(
        "http://api.nbp.pl/api/exchangerates/tables/C?format=json")

    data = response.json()

    return data


def get_rates():
    data = get_data()

    if data:
        return data[0].get("rates", [])

    return []
