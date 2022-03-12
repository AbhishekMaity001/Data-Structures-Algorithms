def fibonacci(n):
    if n<=0:
        print("Please enter a value greater than 2 and not 0!")
    elif n==1:
        print(0)
    elif n==2:
        print(0, 1)
    else:
        a = 0
        b = 1
        print(a)
        print(b)
        while n>2:
            c = a+b
            print(c)
            a, b = b, c
            n = n- 1

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

if __name__ == '__main__':
    count=6
    if count<=0:
        print("Enter value more than 2 only!")
    else:
        for i in range(count):
            print(fib(i), end=" ")

