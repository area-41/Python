"""Quebrando Recordes

"""

def breakingRecords(scores):
    games = scores[0]
    record = scores[1][0]
    lowest = scores[1][0]
    n_breaks = 0
    n_lowest = 0
    for i in scores[1]:
        if i > record:
            record = i
            n_breaks +=1
        if i < lowest:
            lowest = i
            n_lowest += 1
    return n_breaks, n_lowest

if __name__ == '__main__':
    print(breakingRecords([9, [10, 5, 20, 20, 4, 5, 2, 25, 1]]))
    print(breakingRecords([10, [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]]))
