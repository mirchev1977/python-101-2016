# Integer prime factorization
def recursion(n, divider, counter):
    if n % divider == 0:
        n /= divider
        counter += 1
        outp = recursion(n, divider, counter)
        n = outp[0]
        counter = outp[1]

    return [n, counter]




def prime_factorization(n):
    prime_numbers = [2, 3, 5, 7]
    output = []
    for divider in prime_numbers:
        if n % divider == 0:
            outp = recursion(n, divider, 0)
            n = outp[0]
            counter = outp[1]
            ls = (divider, counter)
            output.append(ls)
    if n > 1:
        output.append((n, 1))
    print(output)


prime_factorization(1000)
