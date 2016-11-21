# Is Number Ballanced
def is_number_balanced(n):
    string = str(n)
    middle = len(string) // 2
    front = 0
    back = 0
    if len(string) % 2 == 0:
        front = string[:middle]
        back = string[middle:]
    else:
        front = string[:middle]
        back = string[middle + 1:]

    sum_1 = sum([int(x) for x in front])
    sum_2 = sum([int(x) for x in back])

    if sum_1 == sum_2:
        return True
    else:
        return False


print(is_number_balanced(9))
print(is_number_balanced(4518))
print(is_number_balanced(28471))
print(is_number_balanced(1238033))
