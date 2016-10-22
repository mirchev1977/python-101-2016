# numbers to message
def numbers_to_message(keystrokes):
    chunk = []
    output = []
    first = keystrokes[0]
    index = 0
    while len(keystrokes) > 0:
        if keystrokes[index] == first:
            chunk.append(first)
            if len(keystrokes) > len(chunk):
                index += 1
            else:
                output.append(chunk)
                break
        else:
            output.append(chunk)
            del keystrokes[:len(chunk)]
            chunk = []
            first = keystrokes[0]
            index = 0

    dictionary = {
        "-1": "",
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": "0"}


    capital = False
    outp = ''
    for strokes in output:
        if strokes[0] == 1:
            capital = True
        elif strokes[0] == -1:
            capital = False
            continue
        else:
            key_stroke = strokes[0]
            pressed_times = 0
            if key_stroke == 7 or key_stroke == 9:
                pressed_times = len(strokes) % 4
            elif key_stroke == 0:
                pressed_times = len(strokes) % 1
            else:
                pressed_times = len(strokes) % 3
            combination = list(dictionary[str(key_stroke)])
            current = combination[(pressed_times - 1)]
            if capital == True:
                current = current.upper()
            if current == "0":
                current = " "
            outp += current
            capital = False

    return  outp


print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))
print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
print(numbers_to_message([2, 2, 2, 2]))
