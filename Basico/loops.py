if __name__ == '__main__':
    n = int(input())
    list = []
    while n > 0:
       n -= 1
       list.append(n)

    for i in list:
        print(list[i]**2)