# reduce file path


def reduce_file_path(path):
    cleaned = path.split('/')
    filtered = list(filter(None, cleaned))
    filtered = list(filter(lambda a: a != '.', filtered))

    result = []
    if filtered:
        for i in range(len(filtered)):
            if filtered[i] == '..':
                del result[-1]
            else:
                result.append(filtered[i])

    output = '/' + '/'.join(result)
    return output


def main():
    print(reduce_file_path("/srv/www/./htdocs/wtf"))
    print(reduce_file_path("/"))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/etc/../etc/../etc/../"))


if __name__ == '__main__':
    main()
