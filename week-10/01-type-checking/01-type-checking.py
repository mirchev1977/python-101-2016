import sys
import re


def spl_funct_elements(funct):
    # ['f', '::', 'String', '->', 'Int']
    # ['g', '::', 'Int', '->', 'String']
    lst = funct.split(' ')
    dictionary = {"f_name": lst[0], "f_inp": lst[2], "f_outp": lst[4]}
    return dictionary


def main():
    # inpt = list(sys.stdin)
    inpt = input()

    res = [x.strip('\n') for x in inpt]
    functions = []

    for x in res:
        if x == '':
            break

        functions.append(spl_funct_elements(x))

    last = inpt[-1]
    last = last.split('.')
    last[1] = last[1][:-1].strip()
    last[0] = last[0].strip()

    for x in functions:
        if functions['f_name'] == last[0]:
            print('yes')


if __name__ == '__main__':
    main()


# inp = input('write here: ')
# # ['f :: String -> Int\n', 'g :: Int -> String\n', '\n', 'f . g\n']

# for x in inp:
#   print(x)
