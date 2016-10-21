# Word Counter
def word_counter(inp):
    word = inp[0]
    inp.remove(word)
    dimensions = inp[0]
    inp.remove(dimensions)
    dimensions = dimensions.split(" ")
    dimensions = [int(x) for x in list(dimensions) if x != ' ']

    total_ocurences = 0

    # search horizontally
    for row in range(int(dimensions[0])):
        current = list(inp[row])
        current = [x for x in current if x != ' ']
        current = "".join(current)
        occurences = current.count(word)
        total_ocurences += occurences

        current = current[::-1]
        occurences = current.count(word)
        total_ocurences += occurences

    # create list of char lists
    list_of_char_lists = []
    for row in inp:
        row = [x for x in row if x != ' ']
        list_of_char_lists.append(row)

    # search vertically
    for col in range(int(dimensions[1])):
        current_word = ''
        for row in range(dimensions[0]):
            char = list_of_char_lists[row][col]
            current_word += char
        occurences = current_word.count(word)
        total_ocurences += occurences
        current_word = current_word[::-1]
        occurences = current_word.count(word)
        total_ocurences += occurences

    # search left diagonal - along columns
    row_length = dimensions[0]
    for col in range(0, dimensions[1]):
        current_word = ''
        col_picker = col
        for row in range(row_length):
            char = list_of_char_lists[row][col_picker]
            current_word += char
            col_picker += 1
        row_length -= 1
        occurences = current_word.count(word)
        total_ocurences += occurences
        current_word = current_word[::-1]
        occurences = current_word.count(word)
        total_ocurences += occurences

    # search left diagonal - along rows
    col_end = dimensions[0] - 1
    for row in range(1, dimensions[0]):
        current_word = ''
        row_pointer = row
        for col in range(col_end):
            char = list_of_char_lists[row_pointer][col]
            current_word += char
            row_pointer += 1
        occurences = current_word.count(word)
        total_ocurences += occurences
        current_word = current_word[::-1]
        occurences = current_word.count(word)
        total_ocurences += occurences
        col_end -= 1

    # search right diagonal - along columns
    row_end = 1
    for col in range(dimensions[0] - 1):
        current_word = ''
        col_pointer = col
        for row in range(row_end):
            char = list_of_char_lists[row][col_pointer]
            current_word += char
            col_pointer -= 1
        occurences = current_word.count(word)
        total_ocurences += occurences
        current_word = current_word[::-1]
        occurences = current_word.count(word)
        total_ocurences += occurences
        row_end += 1

    # search right diagonal - along rows
    # col_end = dimensions[1]
    # for row in range(1, dimensions[0]):
    #     current_word = ''
    #     col_pointer = dimensions[1] - 1
    #     row_pointer = row
    #     for col in range(col_end):
    #         char = list_of_char_lists[row_pointer][col_pointer]
    #         current_word += char
    #         col_pointer -= 1
    #         row_pointer += 1
    #     occurences = current_word.count(word)
    #     total_ocurences += occurences
    #     current_word = current_word[::-1]
    #     occurences = current_word.count(word)
    #     total_ocurences += occurences
    #     col_end -= 1

    print(total_ocurences)


inp = ["ivan",
       "5 4",
       "i v a n",
       "e v n h",
       "i n a v",
       "m v v n",
       "q r i t"]

# inp = [
#     "actually",
#     "8 15",
#     "i v a n q h r e z g t z o y m",
#     "e v n h t r x e k y d a i l c",
#     "i a c t u a l l y m c x r l e",
#     "m v c n p u a m n t l u e a a",
#     "q r i t w e a q u p r x t u z",
#     "p e a c t u a l l y w p y t m",
#     "o y h t r e l u f p q n z c s",
#     "p a c t u a l l y u r e q a r"
# ]

word_counter(inp)
