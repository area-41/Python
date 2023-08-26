""" Capitalizar os Nomes
Consiste em dividir a string recebida e imprimir com a primeira letra maiúscula.
Caso comece com números ou caracteres especiais a string não muda.
Caso tenha espaço, o primeiro nome e sobrenome com a 1a letra maiúscula.
"""

def check(s):
    for i in s:
        print(f"\nAntes da mudança: {i}")
        #  divide nos espaços e capitaliza cada pedaço
        a=[j.capitalize() for j in i.split(" ")]
        print("\t"," ".join(a))


if __name__ == '__main__':
    s = ["12abc", "eduardo alcantara", "2BPAnalise cliniCa",
         ":DEpartamento escola", "1 coronel 2 almeidinha 3bp"]
    check(s)
