from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Permite consumir el API de Codigo Facilito'
PACKAGE_NAME = 'codfacapipy'
AUTHOR = 'aleco_rodri'
EMAIL = 'aleco.rodri@gmail.com'
GITHUB_URL = 'alecorodri/codfacapipy'

setup(
    name = PACKAGE_NAME,
    packages = [DESCRIPTION],
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)