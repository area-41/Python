"""
Função que retorna a soma mínima e a máximo dos números digitados
"""

def miniMaxSom(lista):
    lista.sort()
    print(f"lista ordenada: {lista}".format(lista))
    minimo = sum(lista[0:4])
    maximo = sum(lista[1:5])
    print(f"Mínimo: {minimo} - Máximo: {maximo}".format(minimo, maximo))


if __name__ == '__main__':
    lista = []
    for i in range(5):
        lista.append(int(input('Insira um número: ')))

    print(f"lista digitada: {lista}")
    miniMaxSom(lista)
