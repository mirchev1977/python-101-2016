# count characters, words or lines
import sys
import re


def main():
    searched = sys.argv[1]
    file1 = sys.argv[2]
    buff = []
    with open(file1, 'r') as data:
        buff.append(data.read())

    if searched == 'words':
        mystr = buff[0]
        wordList = re.sub("[^\w]", " ", mystr).split()
        print(len(wordList))
    elif searched == "chars":
        chars = len(list(buff[0]))
        print(chars)
    else:
        buff = buff[0].split('\n')
        print(len(buff))


if __name__ == "__main__":
    main()
