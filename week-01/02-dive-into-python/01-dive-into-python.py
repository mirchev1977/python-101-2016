# Counting substrings
def count_substrings(haystack, needle):
    return haystack.count(needle)
# print(count_substrings("This is a test string", "is"))
# print(count_substrings("babababa", "baba"))
# print(count_substrings("Python is an awesome language to program in!", "o"))
# print(count_substrings("We have nothing in common!", "really?"))
# print(count_substrings("This is this and that is this", "this"))

# Sum Numbers in Matrix


def sum_matrix(m):
    # sum_of_numbers = 0
    # for x in m:
    #     for y in x:
    #         sum_of_numbers += y
    # return sum_of_numbers
    return sum([sum(sub_list) for sub_list in m])

# print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))


# NaN Expand
def nan_expand(times):
    buff = "Not a " * times
    return buff + "NaN"
# print(nan_expand(1))
# print(nan_expand(2))
# print(nan_expand(3))
# print(nan_expand(4))
# print(nan_expand(5))

# Integer prime factorization
def recursion(n, divider):
    result = []
    n /= divider
    if n % divider == 0:
        result = recursion(n, divider)
    return result


def prime_factorization(n):
    result = []
    dividers = [2, 3, 5, 7]
    for x in dividers:
        if n % x == 0:
            result =recursion(n, x)
            print(result)


prime_factorization(1000)


def max_consecutive(items):
    max_len = 0
    list_of_cut_lists = []

    while len(items) > 0:
        first = items[0]
        counter = 0
        for x in items:
            if x != first:
                break
            counter += 1
        current_list = items[0:counter]
        list_of_cut_lists.append(current_list)
        del items[0:counter]

    for x in list_of_cut_lists:
        current_len = len(x)
        if current_len > max_len:
            max_len = current_len
    return max_len


# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
