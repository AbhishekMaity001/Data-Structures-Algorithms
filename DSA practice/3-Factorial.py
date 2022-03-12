def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)


if __name__ == '__main__':
    print(fact(5))