import numpy as np


def criarBolao(qtd_volante):
    bolao = []
    contador = 1
    while contador <= qtd_volante:
        numeros = np.random.randint(1, 60, 6)
        bolao.append(numeros)
        contador += 1
    return bolao


if __name__ == '__main__':
    jogo = criarBolao(10)
    for i in jogo:
        print(i)
