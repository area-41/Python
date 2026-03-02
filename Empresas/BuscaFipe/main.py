import string
from core.fipe_handler import FipeAPI


def interface_fipe():
    api = FipeAPI()

    print("\n" + "=" * 40)
    print("      CONSULTA TABELA FIPE 2026")
    print("=" * 40)

    # --- PASSO 1: FILTRO POR LETRA ---
    letras_disponiveis = string.ascii_uppercase
    print(f"\nLetras para busca: {' '.join(letras_disponiveis)}")
    letra_escolhida = input("Escolha a letra inicial da MARCA: ").strip().upper()

    if letra_escolhida not in letras_disponiveis:
        print("[Erro] Escolha uma letra de A a Z.")
        return

    # --- PASSO 2: FILTRAR MARCAS ---
    todas_marcas = api.listar_marcas()
    if todas_marcas.empty: return

    # Filtra as marcas cujo nome começa com a letra escolhida
    marcas_filtradas = todas_marcas[todas_marcas['nome'].str.startswith(letra_escolhida)]

    if marcas_filtradas.empty:
        print(f"\nNenhuma marca encontrada com a letra '{letra_escolhida}'.")
        return

    print(f"\nMARCAS COM A LETRA '{letra_escolhida}':")
    print(marcas_filtradas[['codigo', 'nome']].to_string(index=False))

    id_marca = input("\nDigite o CÓDIGO da marca: ")

    # Validação da marca
    if id_marca not in marcas_filtradas['codigo'].values:
        print("[Erro] Código de marca inválido para esta letra.")
        return

    # --- PASSO 3: MODELOS ---
    modelos = api.listar_modelos(id_marca)
    if modelos.empty: return
    print("\nMODELOS DISPONÍVEIS:")
    print(modelos[['codigo', 'nome']].to_string(index=False))
    id_modelo = input("\nDigite o CÓDIGO do modelo: ")

    # --- PASSO 4: ANOS (Com prevenção de Erro 500) ---
    anos = api.listar_anos(id_marca, id_modelo)
    if anos.empty: return
    print("\nANOS DISPONÍVEIS:")
    print(anos[['codigo', 'nome']].to_string(index=False))
    id_ano = input("\nDigite o CÓDIGO do ano (ex: 2020-1): ")

    # Validação do código do ano para evitar erro 500
    if id_ano not in anos['codigo'].values:
        print(f"\n[Erro] O código '{id_ano}' não existe na lista acima.")
        return

    # --- RESULTADO FINAL ---
    resultado = api.buscar_preco_final(id_marca, id_modelo, id_ano)
    if not resultado.empty:
        print("\n" + "X" * 40)
        print(f"VEÍCULO: {resultado['Modelo'].iloc[0]}")
        print(f"VALOR:   {resultado['Valor'].iloc[0]}")
        print(f"MES REF: {resultado['MesReferencia'].iloc[0]}")
        print("X" * 40)


if __name__ == "__main__":
    while True:
        interface_fipe()
        continuar = input("\nDeseja realizar nova busca? (s/n): ").lower()
        if continuar != 's':
            break