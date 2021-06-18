import requests


def getCities(key,link):

    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': link
    }

    response = requests.request("GET", url, headers=headers)

    return response.text