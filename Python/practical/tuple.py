# x = (1,2,3,4,5,6,2,10,2,11,12,2)
# # y = x.index(2)  # Returns the first index of the value 2
# # print(y)  # Output: 1


# y = len(x)  # Returns the length of the tuple
# print(y)  # Output: 12



def func():
    str = "ruhith"
    x= 20
    return str, x

str,x = func()  # Unpacking the returned tuple
print(str)  # Output: ruhith
print(x)  # Output: 20

rp = func()  # rp is a tuple containing the returned values
print(rp)  # Output: ('ruhith', 20)
num = func() # Accessing the second element of the tuple
print(num)  # Output: 20