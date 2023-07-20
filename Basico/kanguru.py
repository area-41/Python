"""
Dois cangurus em uma linha numérica prontos para pular
na direção positiva (ou seja, em direção ao infinito positivo).
    - O primeiro canguru começa no local x1 e
    move-se a uma velocidade de v1 metros por salto.
    - O segundo canguru começa no local x2 e
    move-se a uma velocidade de v2 metros por salto.

Informar se os dois cangurus estão no mesmo local ao mesmo tempo.
Se for possível, retorne SIM, caso contrário, retorne NÃO.
"""


def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 <= v2:
        return "NO"
    if x1 >= x2:
        first = x1 + v1
        second = x2 + v2
        if first == second:
            return "NO"
        else:
            return "YES"
    if v1 > v2:
        first = x1 + v1
        second = x2 + v2
        while first <= second:
            if first == second:
                return "YES"
            else:
                pass
            x1 = first
            first = x1 + v1
            x2 = second
            second = x2 + v2
        return "NO"

if __name__ == '__main__':
    result = kangaroo(0, 3, 4, 2)
    result = kangaroo(43, 2, 70, 2)
    print(result)
