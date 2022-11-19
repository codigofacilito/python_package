from codigofacilito.workshops import unreleased
from codigofacilito.workshops import articles
from codigofacilito.workshops import allWorkshops

def show_articles():
    articles_out = articles()
    punto = 1
    for lista in articles_out['articles']:
        titulo = lista['title']
        autor = lista['author']['name']
        print(f'{punto}. {titulo} - AUTOR : {autor}')
        punto += 1

def show_unreleased():
    unreleased_out = unreleased()
    punto = 1
    for lista in unreleased_out['workshops']:
        dic_datos = lista['workshop']
        titulo = dic_datos['title']
        nivel = dic_datos['level']
        requirements = dic_datos['requirements']
        fecha = dic_datos['release_date']
        print(f'{punto}. {titulo} - FECHA: {fecha}')
        print(f'    NIVEL: {nivel}')
        print(f'    REQUERIDO: {requirements}\n')
        punto += 1

def show_allWorkshops():
    allWorkshops_out = allWorkshops()
    punto = 1
    for lista in allWorkshops_out:
        titulo = lista['title']
        duracion = lista['duration']

        premium = 'No avisa'
        if lista['is_premium']:
            premium = 'Si'
        elif not lista['is_premium']:
            premium = 'No'
        
        print(f'{punto}. {titulo}')
        print(f'    DURACION: {duracion}')
        print(f'    PREMIUM: {premium}\n')
        punto += 1