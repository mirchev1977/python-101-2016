def search(lst, searched, middleIndex):
    if len(lst) == 1 and lst[middleIndex] != searched:
        return "not found"
    if searched == lst[middleIndex]:
        return middleIndex

    lst1 = lst[:middleIndex]
    lst2 = lst[middleIndex:]

    last1 = lst1[-1]

    if last1 == searched:
        return middleIndex

    if lst2[0] == searched:
        return middleIndex + 1

    if searched < last1:
        middleIndex = len(lst1) //2
        return search(lst1, searched, middleIndex)
    else:
        middleIndex = len(lst2) //2
        return search(lst2, searched, middleIndex)



def main():
    lst = [1, 3, 7, 19, 99, 44, 21, 9, 4, 2, 6, 11, 0, -4, 22, 8, 5, 98, 25, 33]
    lst = sorted(lst)
    searched_item = 19
    middleIndex = len(lst) // 2
    # [-4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 19, 21, 22, 25, 33, 44, 98, 99]
    if lst[middleIndex] == searched_item:
        print("searched index: " + middleIndex)

    found = search(lst, searched_item, middleIndex)
    print(found)


if __name__ == "__main__":
    main()