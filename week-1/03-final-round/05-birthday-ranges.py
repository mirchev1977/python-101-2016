# birthday ranges
def birthday_ranges(birthdays, ranges):
    output = []
    for current_range in ranges:
        birthdays_sum = 0
        for x in range(current_range[0], current_range[1] + 1):
            if(x in birthdays):
                n_birthdays = birthdays.count(x)
                birthdays_sum += n_birthdays
        output.append(birthdays_sum)
    return output

print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [
      (4, 9), (6, 7), (200, 225), (300, 365)]))
print(birthday_ranges([1, 2, 3, 4, 5], [
    (1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
