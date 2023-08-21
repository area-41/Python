"""
O Sr. Vincent trabalha em uma empresa de fabricação de capachos.
Um dia, ele desenhou um novo capacho com as seguintes especificações:
    O tamanho do tapete deve ser N x M. (N é um número natural ímpar e é N vezes.)
    O design deve ter 'WELCOME' escrito no centro.
    O padrão de design deve usar apenas '|', '.' e '-' caracteres.
"""


def imprimir(altura, largura):
    for j in range(1, altura, 2):
        print((".|." * j).center(largura, "-"))
    print("WELCOME".center(largura, "-"))
    for j in range(altura-2, 0, -2):
        print((".|." * j).center(largura, "-"))


if __name__ == '__main__':
    infos = input().split(" ")
    altura = int(infos[0])
    largura = int(infos[1])
    imprimir(altura, largura)
    print(f"Altura: {altura} Largura: {largura}")
