# to reverse a given string or array

def rev(n):
    start = 0
    end = len(n)-1
    while start < end :
        n[start], n[end] = n[end], n[start]
        start = start + 1
        end = end - 1
    return n

 # Now by using list slicing
def recursive_reverse(n):
    return n[::-1]




if __name__ == '__main__':
    n=[1,2,3,4,5,6]
    n2=[10,11,12,13,14,15]
    print(rev(n))
    print(recursive_reverse(n2))
    # print(rev(['Abhishek','Maity']))
