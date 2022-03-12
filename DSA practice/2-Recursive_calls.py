def function(n):
    if (n>0):
        print(n)
        function(n-1)
        function(n-1)


def function1(n):
    if (n>0):
        function1(n-1)
        function1(n-1)
        print(n)


def function2(n):
    if (n > 0):
        function2(n - 1)
        print(n)
        function2(n - 1)


if __name__ == '__main__':
    n=3
    function2(3)