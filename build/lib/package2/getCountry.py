import requests



def getCountries():
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries"

    headers = {
        'x-rapidapi-key': "0d8358d49fmshe586bac4d4ffeb4p16e546jsn456dbfd1b477",
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)