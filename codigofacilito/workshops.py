import requests

allWorkshops_endpoint = 'https://codigofacilito.com/api/v2/workshops'
unreleased_endpoint = 'https://codigofacilito.com/api/v2/workshops/unreleased'
articles_endpoint = 'https://codigofacilito.com/api/v2/articles'

def allWorkshops():
    return getResponse(allWorkshops_endpoint)

def unreleased():
    return getResponse(unreleased_endpoint)

def articles():        
    return getResponse(articles_endpoint)

def getResponse(endpoint):
    response = requests.get(endpoint)

    if response.status_code == 200:
        payload = response.json()
        return payload ['data']


