import requests
import json

# URL da API da Receita Federal
URL = "https://api.portaldareceita.gov.br/v1/cnpj/consulta/basica/?razaoSocial="

# Razão social da empresa
razao_social = "Magazine Python LTDA"

# Faz a requisição à API
resposta = requests.get(URL + razao_social)

# Verifica se a requisição foi bem-sucedida
if resposta.status_code == 200:
    # Decodifica a resposta como JSON
    dados = json.loads(resposta.content)

    # Obtém o endereço da empresa
    endereco = dados["dados"]["endereco"]

    # Imprime o endereço
    print(endereco)
else:
    # Imprime uma mensagem de erro
    print("Erro ao buscar o endereço da empresa.")