# !pip install googlemaps
import pandas as pd

import requests
from geopy.geocoders import Nominatim

import requests
from bs4 import BeautifulSoup


def buscar_cep(cep):
    cep = cep.replace("-", "").replace(".", "").replace(" ", "")

    if len(cep) == 8:
        link = f'https://viacep.com.br/ws/{cep}/json/'

        requisicao = requests.get(link)

        print(requisicao)

        dic_requisicao = requisicao.json()

        uf = dic_requisicao['uf']
        cidade = dic_requisicao['localidade']
        bairro = dic_requisicao['bairro']
        return dic_requisicao
    else:
        print("CEP Inválido")


def buscar_endereco(endereco):
    locator = Nominatim(user_agent="myGeoCoder", timeout=10)
    location = locator.geocode(endereco)
    return location


def buscar_informacoes_empresa(nome):
    url = f"https://www.google.com/search?q={'+'.join(nome.split())}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        results = []

        # A 'CLASS_' DEVE SER ATUALIZADA CADA VEZ
        # zloOqf PZPZlf
        # VwiC3b yXK7lf lyLwlc yDYNvb W8l4ac lEBKkf
        # UDZeY OTFaAf
        # LrzXr
        for result in soup.find_all("div", class_="VwiC3b yXK7lf lyLwlc yDYNvb W8l4ac lEBKkf"):
            results.append(result.text)

        return results

    return "Nada, desculpe!"



if __name__ == "__main__":
    nome = "Salware"
    informacoes = buscar_informacoes_empresa(nome)
    print(informacoes)
