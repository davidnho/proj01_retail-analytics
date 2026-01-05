import requests

def get_usd_to_php_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    return response.json()['rates']['PHP']