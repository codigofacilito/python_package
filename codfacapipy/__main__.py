import logging

from codfacapipy import unreleased

"""
info -> 10
debug -> 20
warning -> 30
error -> 40
critical -> 50
"""

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    workshops = unreleased()

    logging.debug('>>> Estamos iniciando la ejecución del paquete')

    logging.debug(workshops)

    logging.debug('>>> Estamos finalizando la ejecución del paquete')