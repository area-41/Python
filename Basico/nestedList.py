"""
Lista aninhadas
"""


def byScore(students):
    return students[1]


if __name__ == '__main__':
    students = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]

    """ VERSÃO COM INPUT ---
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)
    """

    students.sort(key=byScore)
    lowest = students[0][1]
    while students != [] and students[0][1] == lowest:
        # enquanto não estiver vazio e for igual a menor nota
        students.pop(0)

    if students:  # se não está vazio
        lowest = students[0][1]
        second = []
        for i in students:
            if i[1] == lowest:
                second.append(i[0])
        second.sort()
        for i in second:
            print(i)
