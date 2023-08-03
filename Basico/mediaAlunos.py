"""
Dicionário contendo pares chave/valor de nome:[notas] para uma lista de alunos.
Imprima a média da matriz de notas para o nome do aluno fornecido,
mostrando 2 casas após o decimal.
"""
if __name__ == '__main__':
    n = 2
    student_marks = {"Ana": [25, 26.5, 28], "Joao": [26, 28, 30]}

    """  OPÇÃO DE CÓDIGO COM INPUT
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    """
    query_name = input()
    count = 0
    result = 0
    while count < 3:
        result = result + student_marks[query_name][count]
        count += 1
    print(f'{result/3:.2f}'.format(result))  # imprime o resultado com 2 casas decimais
