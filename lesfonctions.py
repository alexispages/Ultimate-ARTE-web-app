import requests

def collect(url):
    try:
        response = requests.get(url)
    except Exception as error:
        print(error)
    return response.json()
