"""
Com uma string a sua tarefa é trocar as caixas.
Converta todas as letras minúsculas em maiúsculas e vice-versa.
"""

def swap_case(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result

if __name__ == '__main__':
    s = "Pythonist 2"
    s2 = "aLÉM DA iMAGINAÇÃO"
    s3 = "mORNIng cALIFornIa 23G"
    # s = input()
    print(swap_case(s))
    print(swap_case(s2))
    print(swap_case(s3))
