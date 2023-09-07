""" Aplicativo de Juros Compostos
    Criar uma função que receba três parâmetros:
    - o valor inicial do investimento,
    - a taxa de juros anual
    - e o período de tempo em anos.
    A função deve calcular e retornar o valor final do investimento
após o período determinado, levando em consideração os juros compostos.
"""


def calcular_juros_compostos():
    # Coleta dos dados
    valor_inicial = float(input("Qual o valor inicial? R$ "))
    taxa_juros = float(input("Informe a taxa de juros (ex.: 0.08): "))
    periodo = int(input("Qual o período (meses): "))

    # Cálculo do Valor pelos Juros em razão do período informado
    valor_final = valor_inicial
    for i in range(0, periodo):
        valor_final += valor_final * taxa_juros

    # Impressão das informações
    print(f"\nValor Inicial: R$ {valor_inicial}, \nValor Final: R$ {valor_final},"
          f" \nJuros de {taxa_juros * 100} % ao mês por {periodo} meses.\n")

    # Arredondamento do valor para 2 casas decimais, para cima ou para baixo.
    sentido = valor_final - round(valor_final, 2)
    if sentido > 0:
        if sentido >= 0.005:
            print("Valor final do investimento: R$", (round(valor_final + 0.005, 2)))
        else:
            print("Valor final do investimento: R$", (round(valor_final - 0.005, 2)))
    if sentido < 0:
        if sentido >= -0.005:
            print("Valor final do investimento: R$", (round(valor_final + 0.005, 2)))
        else:
            print("Valor final do investimento: R$", (round(valor_final - 0.005, 2)))


if __name__ == '__main__':
    calcular_juros_compostos()
