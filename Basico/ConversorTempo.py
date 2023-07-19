def timeConversion(s):
    print(s)
    if s[-2] == 'P':
        x = s.split(':')
        if x[0] == '12':
            x[2] = x[2][0:2]
            time_converted = str(x[0])+":"+str(x[1])+":"+str(x[2])
            return time_converted
        x[0] = int(x[0]) + 12
        x[2] = x[2][0:2]
        time_converted = str(x[0])+":"+str(x[1])+":"+str(x[2])
        return time_converted
    if s[-2] == 'A':
        x = s.split(':')
        x[2] = x[2][0:2]
        if x[0] == '12':
            x[0] = '00'
            time_converted = str(x[0])+":"+str(x[1])+":"+str(x[2])
            return time_converted
        time_converted = str(x[0])+":"+str(x[1])+":"+str(x[2])
        return time_converted


if __name__ == '__main__':
    print(timeConversion('12:05:45AM'))
    print(timeConversion('02:34:20AM'))
    print(timeConversion('00:01:05PM'))
    print(timeConversion('01:01:05PM'))
    print(timeConversion('10:58:55PM'))
