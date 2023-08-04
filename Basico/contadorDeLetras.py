def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

def count_substring2(string, sub_string):
    return {sub_string: string.count(sub_string) for s in set(string)}


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

    print(count_substring2(string, sub_string))