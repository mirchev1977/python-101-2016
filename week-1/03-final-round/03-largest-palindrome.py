# largest palindrome
def check_if_smaller(decreased, initial):
    string = str(decreased)
    str_len = len(string)
    front = ''
    back = ''
    center = ''
    if str_len % 2 == 0:
        middle = str_len // 2
        front = [int(x) for x in list(string[:middle])]
        back = [int(x) for x in list(string[middle:])]
    else:
        middle = str_len // 2
        front = [int(x) for x in list(string[:middle])]
        center = string[middle]
        back = [int(x) for x in list(string[middle + 1:])]

    back = back[::-1]

    if front == back and decreased < initial:
        return True
    else:
        return False


def get_largest_palindrome(n):
    is_smaller = False
    decreased = n
    while is_smaller == False:
        decreased -= 1
        is_smaller = check_if_smaller(decreased, n)

    return decreased

print(get_largest_palindrome(994687))
print(get_largest_palindrome(99))
print(get_largest_palindrome(252))
print(get_largest_palindrome(754649))
