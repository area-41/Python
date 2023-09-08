""" Número aleatório (Randômico)
A seed (semente) é um valor usado para iniciar o Gerador de Números Randômicos.
"""
import random
import pandas as pd
import numpy as np

# Gerar um valor Randômico float entre 0 e 1
print(f"Valor Randômico gerado entre 0 e 1:\n{random.random()}\n")

random.seed(10)
print(f"Valor Randômico gerado com seed=10:\n{random.random()}")

# se usar a mesma seed vai gerar o mesmo número randômico
random.seed(10)
print(f"Usando mesmo seed:\n{random.random()}\n\n")

# Gerar um número de 13 a 27
print(f"Valor Randômico gerado entre 13 e 27:\n{random.randint(13, 27)}")

# Gerar um Série de 5 números
np.random.seed(1)
a = pd.Series(np.random.randint(1, 11, 5))
print(f"Série gerada Randomicamente de 1 a 10:\n{a}\n")

# Gerar um Dataframe Randomicamente com 5 colunas e 10 linhas
linhas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
colunas = ["A", "B", "C", "D", "E"]
np.random.seed(1)
dados = np.random.randint(0, 100, (10, 5))
df = pd.DataFrame(dados, linhas, colunas)
print(f"Dataframe gerado de 10x5:\n{df}\n\n")
