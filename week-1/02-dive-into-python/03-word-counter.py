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
