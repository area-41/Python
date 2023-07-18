def timeConversion(s):
    print(s)
    if s[-2] == 'P':
        x = s.split(':')
        if x[0] == '12':
            x[2] = x[2][0:2]
            resultado = str(x[0])+":"+str(x[1])+":"+str(x[2])
            return resultado
        x[0] = int(x[0]) + 12
        x[2] = x[2][0:2]
        resultado = str(x[0])+":"+str(x[1])+":"+str(x[2])
        return resultado
    if s[-2] == 'A':
        x = s.split(':')
        x[2] = x[2][0:2]
        if x[0] == '12':
            x[0] = '00'
            resultado = str(x[0])+":"+str(x[1])+":"+str(x[2])
            return resultado
        resultado = str(x[0])+":"+str(x[1])+":"+str(x[2])
        return resultado


if __name__ == '__main__':
    s = '12:05:45AM'
    result = timeConversion(s)
    print(result)
