"""
Você recebe dois carimbos de data e hora de uma postagem que
um usuário pode ver em seu feed de notícias no seguinte formato:
        Dia dd Seg aaaa hh:mm:ss +xxxx
 +xxxx representa o fuso horário.

Imprimir a diferença absoluta (em segundos) entre eles.
"""
from datetime import datetime


def time_delta(t1, t2):
    dt1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    dt2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    diffence = abs(dt1 - dt2).total_seconds()
    return str(int(diffence))


if __name__ == '__main__':
    # t = int(input())  # usar este caso o sistema insira o dado
    t = int(3)  # insere o dado automaticamente
    for t_itr in range(t):
        if t_itr == 0:
            # t1 = input()
            # t2 = input()
            t1 = "Sun 10 May 2015 13:54:36 -0700"
            t2 = "Sun 10 May 2015 13:54:36 -0000"
        if t_itr == 1:
            t1 = "Sat 02 May 2015 19:54:36 +0530"
            t2 = "Fri 01 May 2015 13:54:36 -0000"

        if t_itr == 2:
            t1 = "Sat 02 May 2013 19:54:36 +0530"
            t2 = "Fri 01 May 2015 13:54:36 -0000"


        delta = time_delta(t1, t2)
        print(f"\n\tA diferença entre \n{t1} e \n{t2} \n\té de {delta} segundos.")
