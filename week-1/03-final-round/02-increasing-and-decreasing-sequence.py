# Increasing or decreasing sequence
def increasing_or_decreasing(input_list):
    first = input_list[0]
    # check if increasing
    is_increasing = True
    len_inp_list = len(input_list)
    for x in range(1, len_inp_list):
        if input_list[x] != first + 1:
            is_increasing = False
            break
        first = input_list[x]

    if is_increasing == True:
        return "Up!"

    is_decreasing = True
    first = input_list[0]
    # check if decreasing
    for x in range(1, len_inp_list):
        if input_list[x] != first - 1:
            is_decreasing = False
            break
        first = input_list[x]

    if is_decreasing == True:
        return "Down!"
    else:
        return False

print(increasing_or_decreasing([1, 2, 3, 4, 5]))
print(increasing_or_decreasing([9,8,7,6]))
print(increasing_or_decreasing([5,6,-10]))
print(increasing_or_decreasing([1,1,1,1]))
print(increasing_or_decreasing([-5, -4, -3, -2, -1]))
print(increasing_or_decreasing([-1, -2, -3, -4, -5, -6, -7]))
