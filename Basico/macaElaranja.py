"""
A casa de Sam tem uma macieira e uma laranjeira que dão muitos frutos,
determine o número de maçãs e laranjas que caem.
    No diagrama abaixo:
    -A região vermelha denota a casa, onde s é o ponto inicial e t é o ponto final.
    -A macieira fica à esquerda da casa e a laranjeira à direita.
    -Suponha que as árvores estejam localizadas em um único ponto,
        onde a macieira está no ponto a, e a laranjeira está no ponto b.
    -Quando uma fruta cai de sua árvore, ela pousa d unidades de distância de sua árvore de origem ao longo do eixo-x.

    *Um valor negativo de d significa que a fruta caiu unidades à esquerda da árvore
     e um valor positivo de d significa que ela caiu unidades à direita da árvore. *

     https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
"""


def countApplesAndOranges(s, t, a, b, apples, oranges):
    countApples = 0
    countOranges = 0
    for apple in apples:
        queda = a + apple
        if s <= queda <= t:
            countApples += 1
        else:
            continue
    for orange in oranges:
        queda = b + orange
        if s <= queda <= t:
            countOranges += 1
        else:
            continue

    print(countApples)
    print(countOranges)


if __name__ == '__main__':
    countApplesAndOranges(7, 11, 5, 15, [1, 2, 3, -4, 4, 17], [3, 2, -4])
    countApplesAndOranges(7, 11, 5, 15, [1, 2, -3, -4, 4, 13], [-3, -9, 2, -4, -7])
