''' Anos Bissextos
Um dia extra é adicionado ao calendário quase a cada quatro anos como 29 de fevereiro,
 e o dia é chamado de dia bissexto. Ele corrige o calendário pelo fato de que nosso planeta
  leva aproximadamente 365,25 dias para orbitar o sol. Um ano bissexto contém um dia bissexto.

No calendário gregoriano, três condições são usadas para identificar anos bissextos:

    -> O ano que pode ser dividido por 4, é um ano bissexto, a menos que:
       -> O ano que pode ser dividido por 100, NÃO é um ano bissexto, a menos que:
          -> O ano também que é divisível por 400, então é um ano bissexto.

Isso significa que no calendário gregoriano, os anos 2000 e 2400 são bissextos, enquanto 1800, 1900, 2100, 2200, 2300 e 2500 NÃO são anos bissextos.
'''
# --> Solução já no Python com biblioteca calendar
# from calendar import isleap
# print(isleap(1992))


def is_leap(year):
    leap = False
    
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        leap = True

    return leap


print(is_leap(1990)) # FALSE
print(is_leap(1998)) # FALSE
print(is_leap(2100)) # FALSE
print(is_leap(2100)) # FALSE
print(is_leap(2400)) # TRUE
print(is_leap(1992)) # TRUE
