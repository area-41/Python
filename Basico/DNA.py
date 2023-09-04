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


if __name__ == '__main__':
    string = input("Insira a série na qual deseja procurar: ").strip()
    sub_string = input("Digite as letras que procura: ").strip()
    print(f"Foi(ram) encontrada(s) {count_substring(string, sub_string)} vez(es).")
