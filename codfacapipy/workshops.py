import requests

def unreleased():

    """retornar los proximos talleres en codigo facilito
    >>> type(unreleased()) == type(dict())
    true
    """
    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased')

    if response.status_code == 200:
        pyload = response.json()
        return pyload['data']