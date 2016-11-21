import sys

# sum numbers


def main():
    file = sys.argv[1]
    inp = ""
    with open(file, 'r') as data:
        inp = data.read()
    lst = inp.split(" ")

    numbers_sum = sum([int(x) for x in lst])
    print(numbers_sum)


if __name__ == "__main__":
    main()
