import re

# Sum all numbers in a given string


def sum_of_numbers(string):
    string = split_into_integers = re.split("[a-zA-z]", string)
    string = sum([int(x) for x in string if x != ''])
    return string

print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))
