def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)


def combination(n, r):
    if n == r:
        return 1
    return fact(n)/(fact(n-r)*fact(r))


if __name__ == '__main__':
    print(combination(5, 2))

