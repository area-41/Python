"""
A Universidade tem a seguinte política de notas:
    - Cada aluno recebe um na faixa inclusiva de 1 a 100.
    - Qualquer nota menor que 40 é uma nota de reprovação.

    Sam é professor na universidade e gosta de dar uma volta na cabeça de cada aluno de acordo com estas regras:
        - Se a diferença entre a nota e o próximo múltiplo de 5 for menor que 3, arredondar para o próximo múltiplo de 5.
        - Se o valor da nota for menor que 38, nenhum arredondamento ocorrerá, pois o resultado ainda será uma nota de reprovação.
"""


def gradingStudents(grades):
    for i in range(0, len(grades)):
        if grades[i] < 38:
            continue
        else:
            temp = grades[i]  # pega na lista o elemento da ordem
            grades_temp = temp % 5
            # verifica o resto da divisao por 5, se a diferença para 5 for menor de 3
            # ou seja, se o numero for 3 ou 4
            if grades_temp == 3:
                temp = temp + 2  # se for 3 adiciona 2
                grades[i] = temp
            elif grades_temp == 4:
                temp = temp + 1  # se for 4 adiciona 1
                grades[i] = temp
            else:
                continue  # o resto nao muda
    return grades


if __name__ == '__main__':
    list = [4, 73, 69, 38, 33, 44, 58, 77, 39, 34]
    print("Lista oiginal: \n\t", list)
    student = gradingStudents(list)  # lista com  4 notas
    print(f"Notas arredondadas segundo os critérios: \n\t{student}".format(student))
