# cat.py
import sys


def main():
    for file in sys.argv[1:]:
        with open(file, 'r') as data:
            print(data.read())


if __name__ == '__main__':
    main()
