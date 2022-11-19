import logging as log
from codigofacilito import show_articles
from codigofacilito import show_unreleased
from codigofacilito import show_allWorkshops

log.basicConfig(level=log.INFO)

def main():
    log.info(f'ARICULOS...')
    show_articles()

    log.info(f'PROXIMOS WORKSHOPS...')
    show_unreleased()

    log.info(f'TODOS LOS WORKSHOPS...')
    show_allWorkshops()

if __name__ == "__main__":
    log.info(f'INICIANDO... {__name__}')
    main()