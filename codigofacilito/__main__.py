import logging as log
from codigofacilito import articles
from codigofacilito import unreleased
from codigofacilito import allWorkshops

def main():
    show_articles()
    show_unreleased()
    show_allWorkshops()
    
def show_articles():
    articles_out = articles()
    print(articles_out)
    punto = 1
    for lista in articles_out['articles']:
        titulo = lista['title']
        autor = lista['author']['name']
        print(f'{punto}. {titulo} - AUTOR : {autor}\n')
        punto = punto + 1

def show_unreleased():
    unreleased_out = unreleased()
    show(unreleased_out)

def show_allWorkshops():
    allWorkshops_out = allWorkshops()
    show(allWorkshops_out)

def show(dict_out):
    punto = 1
    for lista in dict_out['workshops']:
        titulo = lista['workshop']['title']
        nivel = lista['workshop']['level']
        requirements = lista['workshop']['requirements']
        fecha = lista['workshop']['release_date']
        print(f'{punto}. {titulo} - FECHA: {fecha}')
        print(f'    NIVEL: {nivel}')
        print(f'    REQUERIDO: {requirements}\n')
        punto = punto + 1

if __name__ == "__main__":
    log.debug(f'iniciando... {__name__}')
    main()