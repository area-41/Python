import numpy as np


def velasDeAniversario(velas):
    velas.sort()  # primeiro colocar os números em ordem
    qtd = 0
    *_, ultimo = velas  # adiciona o último número à variável ultimo
    for i in velas:  # contar quantos números iguais ao ultimo
        if i == ultimo:
            qtd += 1
    return qtd


if __name__ == '__main__':
    # função random para criar uma quantidade até 10 aleatória de linhas
    arr = np.random.randint(10, size=6)
    print("\nQtde de linhas: ", arr)

    result = velasDeAniversario(arr)
    print("\nQuantidade de velas mais altas: \n", result)
