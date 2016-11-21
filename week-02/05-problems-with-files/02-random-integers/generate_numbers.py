# generate_numbers.py
import sys
from random import randint
import io


def main(n):
    n = int(n)
    random_numbers = []
    for x in range(n):
        generated = randint(1, 1000)
        random_numbers.append(str(generated))

    concatinated_numbers = " ".join(random_numbers)

    with io.FileIO("numbers.txt", "w") as file:
        bytes_ = str.encode(concatinated_numbers)
        file.write(bytes_)


if __name__ == '__main__':
    main(sys.argv[1])
