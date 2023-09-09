temp_Celsius = [9, 22, 38, 0, -10, 15, 27]


def fahrenheit(c):
    return (9/5)*c+32


print(f'Temperaturas originais em Celsius:\n{temp_Celsius}\n')
print(f'Temperaturas convertidas em Fahrenheit:')
# para adicionar a lista usa apenas += no lugar de append
temp_F = []
for temp in temp_Celsius:
    temp_F += [fahrenheit(temp)]
print(temp_F)

# Usando o append
temp_G = []
for temp in temp_Celsius:
    temp_G.append(fahrenheit(temp))
print(temp_G)

# Usando o map
temp_F2 = list(map(fahrenheit, temp_Celsius))
print(temp_F2)

# Usando função lambda
temp_F3 = list(map(lambda c: (9/5)*c+32, temp_Celsius))
print(temp_F3)
