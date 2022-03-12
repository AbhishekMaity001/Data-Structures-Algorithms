line = input("Enter a string : ")
print("The Entered String is : {}".format(line))
print("The Reverse String is {}".format(line[::-1]))  # Way 1 to reverse a string
# print(len(line))
out = ''
for s in range(len(line)-1, -1, -1):  # Way 2 to reverse a string
    out = out+line[s]
print(out)
