import requests


def buscar_endereco_por_razao_social(razao_social, cnpj, api_key):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    headers = {'Authorization': f'Bearer {api_key}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dados_empresa = response.json()
        return dados_empresa['logradouro'], dados_empresa['numero'], dados_empresa['municipio'], dados_empresa['uf']
    else:
        return None


# Substitua 'SUA_API_KEY' pela chave de acesso fornecida pela Receita Federal
api_key = 'SUA_API_KEY'
razao_social = 'Exemplo LTDA'
cnpj = '00000000000000'  # Substitua pelo CNPJ da empresa que você deseja consultar

endereco = buscar_endereco_por_razao_social(razao_social, cnpj, api_key)

if endereco:
    logradouro, numero, municipio, uf = endereco
    print(f'Endereço: {logradouro}, {numero}, {municipio} - {uf}')
else:
    print('Não foi possível obter o endereço.')
