"""Compreensão de Lista
A compreensão de lista oferece uma sintaxe mais curta
 quando você deseja criar uma nova lista
 com base nos valores de uma lista existente.
"""
if __name__ == '__main__':
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
  meats = ["chicken", "beef", "fish", "pork"]
  list_a = []

  # 1 - version
  for x in fruits:
    if "a" in x:  # procurar frutas que tenha 'a'
      list_a.append(x)

  # 2 - version
  list_e = [x for x in fruits if "e" in x]

  # 3 - version
  list_apple = [x for x in fruits if x != "apple"]

  x = 'banana'
  # 4 - version
  list_noIF = [x for x in fruits]

  print(fruits)
  print("List with 'a': ", list_a)
  print("List with 'e': ", list_e)
  print("List with 'not apple': ", list_apple)
  print("List with 'no IF': ", list_noIF)

  newlist = [x for x in range(10)]  # criar lista de 0 a 10
  print(newlist)
  newlist2 = [x for x in range(10) if x < 5]  # criar lista para < 5
  print(newlist2)
  newlist3 = [x.upper() for x in fruits]
  print(newlist3)

  newlist4 = ['kiwi' for x in fruits] # substituir cada elemento por kiwi
  print(newlist4)

  newlist5 = [x if x != "banana" else "orange" for x in fruits]  # trocar banana por laranja
  print(newlist5)

  h_letters = [ letter for letter in 'human' ]
  print( h_letters)

  letters = list(map(lambda x: x, 'human'))
  print(letters)

  number_list = [x for x in range(20) if x % 2 == 0]
  print(number_list)

  num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
  print(num_list)

  obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
  print(obj)

  transposed = []
  matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

  for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
      transposed_row.append(row[i])
    transposed.append(transposed_row)

  print(transposed)

  matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
  transpose = [[row[i] for row in matrix] for i in range(2)]
  print(transpose)

  x = 1
  y = 1
  z = 2
  n = 3

  new_list = [x for x in range(n)]
  new_list = [y for y in range(n)]
  new_list = [z for z in range(n)]
  print(new_list)

  matrix = [[j for j in range(3)] for i in range(3)]
  print(matrix)

  x = 1
  y = 1
  z = 1
  n = 2
  matrix = [[[[i, j, k] for k in range(n)] for j in range(n)] for i in range(n) if ((x + y + z) != n)]
  print(matrix)

  matrix = [[[[i, j, k] for k in range(x)] for j in range(y)] for i in range(z)]
  print(matrix)

  matrix = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if ((i + j + k) != n)]
  print(matrix)

  matrix = [[i, j, k] for k in range(z) for j in range(y) for i in range(x) if ((x + y + z) != n)]
  print(matrix)
  print("expected: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]")

  matrix = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)]
  print("Answer :", matrix)

  matrix = []
  for i in range(x):
    # Append an empty sublist inside the list
    matrix.append([(i)])
    for j in range(y):
      matrix[i].append([(j)])
      for k in range(z):
        matrix[i][j].append([(k)])

  print("Matrix:", matrix)