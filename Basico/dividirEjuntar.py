"""
Divida e junte a string passada
"""

def split_and_join(line):
    # dividir
    line = line.split(" ")  # convertido em uma lista

    # juntar
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)