# message to numbers
def message_to_numbers(message):
    # message_list = list(message)

    output = []
    key_digit = ''
    index = None
    current_char = ''
    for char in message:
        current_string = ''
        if char.lower() in "abc":
            current_string = "abc"
            key_digit = 2
        elif char.lower() in "def":
            current_string = "def"
            key_digit = 3
        elif char.lower() in "ghi":
            current_string = "ghi"
            key_digit = 4
        elif char.lower() in "jkl":
            current_string = "jkl"
            key_digit = 5
        elif char.lower() in "mno":
            current_string = "mno"
            key_digit = 6
        elif char.lower() in "pqrs":
            current_string = "pqrs"
            key_digit = 7
        elif char.lower() in "tuv":
            current_string = "tuv"
            key_digit = 8
        elif char.lower() in "wxyz":
            current_string = "wxyz"
            key_digit = 9
        elif char.lower() in " ":
            current_string = " "
            key_digit = 0

        index = current_string.index(char.lower())
        if char == char.upper() and char != " ":
            output.append("1")
        if str(key_digit).lower() == current_char.lower():
            output .append("-1")
        current_char = str(key_digit)
        output.append(str(int(str(key_digit) * (index + 1))))
        index = None

    output = [int(x) for x in output]
    outp_lst = []
    for x in output:
        if x == -1:
            outp_lst.append(x)
        else:
            x = list(str(x))
            outp_lst.extend([int(i) for i in x])
    return outp_lst


print(message_to_numbers("Ivo e Panda"))
print(message_to_numbers("aabbcc"))
print(message_to_numbers("abc"))
print(message_to_numbers("a"))
