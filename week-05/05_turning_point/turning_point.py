def find_turning_point(lst, middle, start, end):
    if lst[middle] < lst[middle - 1]:
        return middle

    start = middle
    end = len(lst)
    middle = (start + end) // 2
    return find_turning_point(lst, middle, start, end)


def main():
    # lst = [1, 3, 7, 9, 4, 2]
    # lst = [1, 6, 4, 3, 2]
    # lst = [1, 4, 5, 2]
    # lst = [1, 3, 7, 9, 12, 18, 9, 8, 7, 6, 2]
    # lst = [1, 3, 7, 9, 12, 11, 9, 8, 7, 6, 2]
    # lst = [1, 3, 7, 9, 12, 11, 9, 8, 7, 6, 2]
    # lst = [1, 3, 2, 1, 0, -1]
    middle = len(lst) // 2
    start = 0
    end = len(lst)
    turning_point = find_turning_point(lst, middle, start, end)
    print(turning_point, lst[turning_point])

if __name__ == "__main__":
    main()