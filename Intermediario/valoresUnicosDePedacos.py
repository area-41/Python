"""
Imprimir valores únicos de pedaços de tamanho 'k' de uma 'string' dada.
"""


def merge_the_tools(string, k):
    while string:
        pedaco, string = string[:k], string[k:] # quebra o pedaco tamanho k
        temp = ""
        for char in pedaco:  # para cada 'char' adiciona em 'temp' se não existir ainda
            if char not in temp:
                temp += char
        print(temp)

        # unicos = ''.join(sorted(set(pedaco)))
        # Se for colocar em ordem
        # unicos_ordem = ''.join(sorted(set(pedaco)))
        # print(unicos)


if __name__ == '__main__':
    # string, k = input(), int(input())
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)
