# credit card validation


def is_credit_card_valid(number):
    lst = list(str(number))

    for i in range(len(lst)):
        if i % 2 != 0:
            current = int(lst[i]) * 2
            lst[i] = str(current)

    string = "".join(lst)

    sum_digits = sum([int(x) for x in string])

    if sum_digits % 10 == 0:
        return True
    else:
        return False


def main():
    print(is_credit_card_valid(79927398713))
    print(is_credit_card_valid(79927398715))


if __name__ == "__main__":
    main()
