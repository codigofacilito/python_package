import requests

#pruebas con python -m doctest workshops.py
allWorkshops_endpoint = 'https://codigofacilito.com/api/v2/workshops'
unreleased_endpoint = 'https://codigofacilito.com/api/v2/workshops/unreleased'
articles_endpoint = 'https://codigofacilito.com/api/v2/articles'

def allWorkshops():
    """Retorna todos los talleres de codigofacilito
    >>> type(allWorkshops()) == type(list())
    True
    """
    return getResponse(allWorkshops_endpoint)

def unreleased():
    """Retorna proximos talleres en codigofacilito
    >>> type(unreleased()) == type(dict())
    True
    """
    return getResponse(unreleased_endpoint)

def articles():
    """Retorna articulos de codigofacilito
    >>> type(articles()) == type(dict())
    True
    """        
    return getResponse(articles_endpoint)

def getResponse(endpoint):
    """Retorna diccionario con la respuesta al request del endpoint dado
    >>> type(getResponse(allWorkshops_endpoint)) == type(list())
    True
    >>> type(getResponse(unreleased_endpoint)) == type(dict())
    True
    >>> type(getResponse(articles_endpoint)) == type(dict())
    True
    """
    response = requests.get(endpoint)

    if response.status_code == 200:
        payload = response.json()
        return payload ['data']

