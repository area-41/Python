"""
retornar True/False em 5 linhas sendo:
    1 linha - se tem número
    2 linha - se tem letra do alfabeto
    3 linha - se tem dígitos
    4 linha - se tem letras minúsculas
    5 linha - se tem letras maiúsculas
"""


def stringValidator(s):
    for i in range(1, 6):
        if s.isalnum():
            print('True')
        elif s.isalpha():
            print('True')
        elif s.isdigit():
            print('True')
        elif s.islower():
            print('True')
        elif s.isupper():
            print('True')
        else:
            print('False')


if __name__ == '__main__':
    s = input()
    stringValidator(s)
