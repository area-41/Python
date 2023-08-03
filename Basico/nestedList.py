"""

"""
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)

    students.sort()
    students.pop(0)
    lowest = students[0]
    for j in students:
        if j[1] < lowest[1]:
            lowest = j
    for i in students:
        if i[1] == lowest[1]:
            print(i[0])
