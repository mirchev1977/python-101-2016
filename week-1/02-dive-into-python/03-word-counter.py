def iterate_diagonals(inp, matrix_rows, matrix_cols, searched_word):
    total_ocurences = 0
    shorten = False
    rows_reach = matrix_rows
    cols_reach = matrix_cols
    for col in range(cols_reach):
        curr_col = col
        buff = ''
        for row in range(rows_reach):
            buff += inp[row][curr_col]
            curr_col += 1
            if row == matrix_rows - 2 and curr_col == matrix_cols - 1:
                shorten = True
        if shorten == True:
            rows_reach -= 1
        ocurrences = buff.count(searched_word)
        total_ocurences += ocurrences
        buff = buff[::-1]
        ocurrences = buff.count(searched_word)
        total_ocurences += ocurrences
    return total_ocurences

# Word Counter
def word_counter(inp):
    searched_word = inp[0]
    inp.remove(searched_word)
    dimensions = inp[0]
    inp.remove(dimensions)
    dimensions = dimensions.split(" ")
    dimensions = [int(x) for x in dimensions]
    matrix_rows = dimensions[0]
    matrix_cols = dimensions[1]
    total_ocurences = 0

    for x in range(len(inp)):
        val = inp[x].split(' ')
        inp[x] = val

    # iterate rows horizontally
    for x in range(matrix_rows):
        current_row = "".join(inp[x])
        ocurrences = current_row.count(searched_word)
        total_ocurences += ocurrences
        current_row = current_row[::-1]
        ocurrences = current_row.count(searched_word)
        total_ocurences += ocurrences

    # iterate cols vertically
    for col in range(matrix_cols):
        buff = ''
        for row in range(0, matrix_rows):
            buff += inp[row][col]
        ocurrences = buff.count(searched_word)
        total_ocurences += ocurrences
        buff = buff[::-1]
        ocurrences = buff.count(searched_word)
        total_ocurences += ocurrences

    # iterate along cols left - right and rows top - bottom
    total_ocurences += iterate_diagonals(inp, matrix_rows, matrix_cols, searched_word)

    # create different shapes matrices
    matrix_1 = inp[::-1]

    matrix_2 = []
    for x in matrix_1:
        x = x[::-1]
        matrix_2.append(x)

    matrix_3 = matrix_2[::-1]

    print(total_ocurences)


"""
# inp = ["ivan",
#        "5 4",
#        "i v a n",
#        "e v n h",
#        "i n a v",
#        "m v v n",
#        "q r i t"]
"""

inp = [
    "actually",
    "8 15",
    "i v a n q h r e z g t z o y m",
    "e v n h t r x e k y d a i l c",
    "i a c t u a l l y m c x r l e",
    "m v c n p u a m n t l u e a a",
    "q r i t w e a q u p r x t u z",
    "p e a c t u a l l y w p y t m",
    "o y h t r e l u f p q n z c s",
    "p a c t u a l l y u r e q a r"
]

word_counter(inp)
