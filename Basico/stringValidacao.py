"""
retornar True/False em 5 linhas sendo:
    1 linha - se tem número
    2 linha - se tem letra do alfabeto
    3 linha - se tem dígitos
    4 linha - se tem letras minúsculas
    5 linha - se tem letras maiúsculas
"""


def stringValidator(s):
    list = []

    opcao = []
    for char in s:
        opcao.append(str.isalnum(char))
    if True in opcao:
        list.append(True)
    else:
        list.append(False)


    opcao = []
    for char in s:
        opcao.append(str.isalpha(char))
    if True in opcao:
        list.append(True)
    else:
        list.append(False)

    opcao = []
    for char in s:
        opcao.append(str.isdigit(char))
    if True in opcao:
        list.append(True)
    else:
        list.append(False)

    opcao = []
    for char in s:
        opcao.append(str.islower(char))
    if True in opcao:
        list.append(True)
    else:
        list.append(False)

    opcao = []
    for char in s:
        opcao.append(str.isupper(char))
    if True in opcao:
        list.append(True)
    else:
        list.append(False)

    for elem in list:
        print(elem)



if __name__ == '__main__':
    # s = input()
    s = 'qA2'
    stringValidator(s) # retorno esperado T,T,T,T,T

    stringValidator('123') # retorno esperado T, F, T, F, F
