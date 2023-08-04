"""
Dada uma sequência de letras(string), procure quantas vezes
uma tríade de letras(sub_string) se repete.
"""


def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:].startswith(sub_string):  # StartsWith usado para fazer a comparação
            count += 1
    return count


def count_substring2(string, sub_string):
    return {s: string.count(sub_string) for s in set(string)}


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    print(count_substring(string, sub_string))
    print(count_substring2(string, sub_string))
