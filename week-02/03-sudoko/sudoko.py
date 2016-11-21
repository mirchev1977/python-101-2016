# sudoko


def check_squares(sudoko):
    for row in range(0, len(sudoko), 3):
        for col in range(0, len(sudoko), 3):
            row_lst = []
            row_lst.append(sudoko[row][col])
            row_lst.append(sudoko[row][col + 1])
            row_lst.append(sudoko[row][col + 2])
            row_lst.append(sudoko[row + 1][col])
            row_lst.append(sudoko[row + 1][col + 1])
            row_lst.append(sudoko[row + 1][col + 2])
            row_lst.append(sudoko[row + 2][col])
            row_lst.append(sudoko[row + 2][col + 1])
            row_lst.append(sudoko[row + 2][col + 2])
            row_lst = sorted(row_lst)
            if row_lst != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
    return True


def check_horizontals(sudoko):
    for row in sudoko:
        row_sorted = sorted(row)
        if row_sorted != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True


def check_verticals(sudoko):
    for col in range(len(sudoko)):
        lst = []
        for row in range(len(sudoko)):
            lst.append(sudoko[row][col])
        lst = sorted(lst)
        if lst != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True


def sudoku_solved(sudoko):
    squares = check_squares(sudoko)

    if squares == False:
        return False

    horizontals = check_horizontals(sudoko)
    if horizontals == False:
        return False

    verticals = check_verticals(sudoko)
    if verticals == False:
        return False

    return True


def main():
    print(sudoku_solved([
        [4, 5, 2, 3, 8, 9, 7, 1, 6],
        [3, 8, 7, 4, 6, 1, 2, 9, 5],
        [6, 1, 9, 2, 5, 7, 3, 4, 8],
        [9, 3, 5, 1, 2, 6, 8, 7, 4],
        [7, 6, 4, 9, 3, 8, 5, 2, 1],
        [1, 2, 8, 5, 7, 4, 6, 3, 9],
        [5, 7, 1, 8, 9, 2, 4, 6, 3],
        [8, 9, 6, 7, 4, 3, 1, 5, 2],
        [2, 4, 3, 6, 1, 5, 9, 8, 7]
    ]))

    print(sudoku_solved([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]))


if __name__ == '__main__':
    main()
