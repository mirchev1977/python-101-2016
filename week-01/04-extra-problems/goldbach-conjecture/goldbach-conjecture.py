import collections

# goldbach conjecture


def check_if_prime(n):
    is_prime = True
    for i in range(2, n, 1):
        if n % i == 0:
            is_prime = False
            break

    return is_prime


def goldbach(n):
    output_lst = []
    dictionary = {}
    for i in range(2, n, 1):
        is_prime = check_if_prime(i)
        # find second member
        if is_prime:
            second_member = n - i
            second_is_prime = check_if_prime(second_member)
            if second_is_prime:
                tupl = (i, second_member)
                dictionary[i] = tupl

    sorted_list = collections.OrderedDict(sorted(dictionary.items()))

    for x in sorted_list:
        if sorted_list[x][0] <= sorted_list[x][1]:
            output_lst.append(sorted_list[x])

    return output_lst


def main():
    print(goldbach(4))
    print(goldbach(6))
    print(goldbach(8))
    print(goldbach(10))
    print(goldbach(100))


if __name__ == '__main__':
    main()
