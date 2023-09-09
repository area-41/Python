""" Variações de função lambda
Também chamada de funções anônimas, são funções definidas
anonimamente e em uma única linha.
"""

quadrado = lambda num: num * num
print(f"Quadradro usando lambda: {quadrado(4)}")

par = lambda num: num % 2 == 0
print(f"O número é par: {par(3)}")

first = lambda x: x[0]
print(f"{first('Hello World')}")

inverte = lambda x: x[::-1]
hw = inverte("Tudo tranquilo aqui na colônia.")
print(hw)

print(inverte('Podemos mandar qualquer mensagem invertida'))
