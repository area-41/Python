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