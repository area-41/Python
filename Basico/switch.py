def switch(function):
    if function == "insert":
        function.split()
        print(function[1])
        return list.insert(function[1], function[2])
    elif function == "remove":
        function.split()
        list.remove(function[1])
    elif function == "append":
        function.split()
        print(function[1])
        return list.append(function[1])
    elif function == "sort":
        list.sort()
    elif function == "pop":
        list.pop()
    elif function == "reverse":
        list.reverse()
    elif function == "print":
        return list


if __name__ == '__main__':
    list = []
    N = int(input())
    count = 1
    while count <= N:
        escolha = input("Insira o comando: ")
        #switch(str(function))
        function = escolha.split()
        if function[0] == "insert":
            list.insert(int(function[1]), int(function[2]))
        elif function[0] == "remove":
            list.remove(int(function[1]))
        elif function[0] == "append":
            list.append(int(function[1]))
        elif function[0] == "sort":
            list.sort()
        elif function[0] == "pop":
            list.pop()
        elif function[0] == "reverse":
            list.reverse()
        elif function[0] == "print":
            print(list)
        count += 1
    print(list)


"""
def switch_case(option):
    match option:
        case 'insert':
            list.insert(N[1], N[2])
        case 'remove':
            list.remove(N[1])
        case 'append':
            list.append(N[1], N[2])
        case 'sort':
            list.sort()
        case 'pop':
            list.pop()
        case 'reverse':
            list.reverse()
        case 'print':
            print(list)
        case _:
            return 'Opção inválida'


if __name__ == '__main__':
    N = int(input())
    list = []

    option = int(input())
    result = switch_case(option)
    print(result)

"""