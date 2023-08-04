"""

"""


def mutate_string(string, position, character):
    # quebra a string na posição desejada e adiciona o caracter mais o outro pedaço da string
    string = string[:position] + character + string[position+1:]
    return string


def mutate_string2(string, position, character):
    # outra solução mas usando a quebra em lista e juntando depois
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

    s2 = input()
    i2, c2 = input().split()
    s_new = mutate_string2(s2, int(i2), c2)
    print(s_new)
