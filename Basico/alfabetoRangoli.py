""" Alfabeto Rangoli
Você recebe um número inteiro N e sua tarefa é imprimir um alfabeto rangoli de tamanho N.
(Rangoli é uma forma de arte popular indiana baseada na criação de padrões.)
    O centro do rangoli tem a primeira letra do alfabeto a, e o limite tem o
    tamanho equivalente de letra do alfabeto (em ordem alfabética).
Descrição da função:
    Rangoli possui os seguintes parâmetros:
        tamanho interno: o tamanho do Rangoli
Devoluções
    String: uma única String composta por cada uma das linhas do Rangoli
    separadas por um caractere de nova linha (\n)
Formato de entrada:
    Apenas uma linha de entrada contendo o tamanho do Rangoli.
Restrições:
    0 < tamanho < 27

-----> Exemplo de entrada: 5
Saída:
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
import string


def print_rangoli(size):
    """linha central, composta por letra do alfabeto do tamanho até a letra "a"
    para isso diminui 1 do tamanho, e multiplica por 4, porque são 2 vezes(para ir e voltar)
    e porque dobra por ter o caracter hífen, mais 1 que representa a letra central da linha."""

    central_line = 4*(size - 1) + 1
    letters = list(string.ascii_lowercase)[0:size]
    letters_r = letters[::-1]

    # Para usar o sistema nativo chr sem precisar importar o string, mas a partir do 97 é caracter romano
    # letters = [chr(i + 97) for i in range(size)]
    # letters_r = [chr(size - i + 96) for i in range(size)]

    # Descrição:
    print(f"Para o tamanho {size}, gerou {central_line} caracteres na linha central,"
          f"\nresultante do cálculo:"
          f"\n\t central_line = 4*({size} - 1) + 1"
          f"\n\ncom as seguintes listas de letras:"
          f"\n{letters}"
          f"\n{letters_r}"
          f"\n\nFormando a figura:")

    # parte de cima da figura
    for i in range(size):
        print('-'.join(letters_r[:i + 1] + letters[size - i:]).center(central_line, '-'))
    # parte de baixo da figura
    for i in range(size - 1):
        print('-'.join(letters_r[:size - i - 1] + letters[i + 2:]).center(central_line, '-'))


if __name__ == '__main__':
    # n = int(input())
    size = int(input("Digite número do tamanho que vc deseja construir: ")) # a letra z representa o número 26
    print_rangoli(size)
