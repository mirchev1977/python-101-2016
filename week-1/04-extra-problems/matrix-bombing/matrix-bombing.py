import copy


def turn_into_matrix(m):
    for row in range(len(m)):
        current_row = m[row].split(" ")
        current_row = filter(None, current_row)
        m[row] = [int(x) for x in current_row]

        # [[10, 10, 10],
        # [10, 9, 10],
        # [10, 10, 10]]
    return m


def validate_neighbors(row, col, m):
    valid_neighbors = []
    row_above = row - 1
    row_below = row + 1
    row_same = row

    col_left = col - 1
    col_same = col
    col_right = col + 1

    # dictionary = {"row": 0, "col": 0}

    if row_above >= 0:
        if col_left >= 0:
            dictionary = {'row': None, 'col': None}
            dictionary['row'] = row_above
            dictionary['col'] = col_left
            valid_neighbors.append(dictionary)
        if col_same >= 0:
            dictionary = {'row': None, 'col': None}
            dictionary['row'] = row_above
            dictionary['col'] = col_same
            valid_neighbors.append(dictionary)
        if col_right <= len(m) - 1:
            dictionary = {'row': None, 'col': None}
            dictionary['row'] = row_above
            dictionary['col'] = col_right
            valid_neighbors.append(dictionary)

    if row_same >= 0:
        if col_left >= 0:
            dictionary = {'row': None, 'col': None}
            dictionary['row'] = row_same
            dictionary['col'] = col_left
            valid_neighbors.append(dictionary)
        if col_right <= len(m) - 1:
            dictionary = {'row': None, 'col': None}
            dictionary['row'] = row_same
            dictionary['col'] = col_right
            valid_neighbors.append(dictionary)

    if row_below <= len(m) - 1:
        if col_left >= 0:
            dictionary = {'row': None, 'col': None}
            dictionary['row'] = row_below
            dictionary['col'] = col_left
            valid_neighbors.append(dictionary)
        if col_same >= 0:
            dictionary = {'row': None, 'col': None}
            dictionary['row'] = row_below
            dictionary['col'] = col_same
            valid_neighbors.append(dictionary)
        if col_right <= len(m) - 1:
            dictionary = {'row': None, 'col': None}
            dictionary['row'] = row_below
            dictionary['col'] = col_right
            valid_neighbors.append(dictionary)

    return valid_neighbors


def bomb(int_val, row, col, m):
    # validate neighbors
    valid_neighbors = validate_neighbors(row, col, m)
    matrix = copy.deepcopy(m)

    for neighbor in valid_neighbors:
        neighbor_value = m[neighbor['row']][neighbor['col']]
        remainder = neighbor_value - int_val
        if remainder < 0:
            remainder = 0

        matrix[neighbor['row']][neighbor['col']] = remainder

    sum_matrix = sum([sum(x) for x in matrix])

    return sum_matrix


# matrix bombing
def matrix_bombing_plan(m):
    # create a copy of matrix filled with zeros
    m = turn_into_matrix(m)

    dictionary = {}

    # iterate over matrix m
    for row in range(len(m)):
        for col in range(len(m[row])):
            int_val = m[row][col]
            matrix_sum = bomb(int_val, row, col, m)
            tpl = (row, col)
            dictionary[tpl] = matrix_sum

    return dictionary


def main():
    """
    10  10  10
    10   9  10
    10  10  10
    """
    # input = ["10  10  10", "10   9  10", "10  10  10"]
    input = ["1  2  3", "4   5  6", "7  8  9"]
    print(matrix_bombing_plan(input))


if __name__ == "__main__":
    main()
