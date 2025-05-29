# # # print("gardencity \\n college")
# # # print((2+3)*4)  

# # # a= 20
# # # b=10
# # # c=15
# # # d=5
# # # e=0
# # # e = (a+b)*c/d
# # # f = ((a+b)*c)/d
# # # g = (a+b)*(c/d)
# # # z= a+(b*c)/d
# # # print("value of (a+b)*c/d) is", z)
# # # print("value of (a+b)*c/d) is", g)
# # # print("value of (a+b)*c/d) is", f)
# # # print("value of (a+b)*c/d) is", e)


# # integer = -29
# # print("The absolute value of", integer, "is", abs(integer))


# # for x in range(3):
# #     print(x)

# # print("Hello, World!")
# # def hello():
# #     print("Hello, !")
# # print("ruhith")
# # print("pasha")
# # hello()

# # def hf():
# #     hello

# # hf()

# def add(x,y):
#     a = x + y
#     b= x - y
#     return a,b
# print(add(10,5))

# def wish(name, msg):
#     print("Hello", name, msg)0-# wish("Ruhith",)

# def func(a, b=5,c=10):
#     print("a is ",a,"and b is ",b,"and c is ",c)

# func(3,7)
# func(25,c=24)
# func(c=50,a=100)

# def wish (*names):
#     for name in names:
#         print("Hello", name)
# wish("Ruhith", "Pasha", "Khan")

# pi = 3.142
# def area(r):
#     return pi * r * r
# r = int(input("Enter the radius of the circle: "))
# print("Area of the circle is: ", area(r))


# def calculate(a,b):
#     total = a + b
#     difference = a - b
#     product = a * b
#     division = a / b
#     mod = a % b

#     return total, difference, product, division, mod
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# s,d,p,q,r= calculate(a, b)
# print("Sum:", s)
# print("Difference:", d)
# print("Product:", p)        
# print("Division:", q)
# print("Modulus:", r)


# def biggest(a,b):
#     if a > b:
#         return a
#     else:
#         return b
    
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# result = biggest(a,b)
# print("The biggest number is: ", result)

# integer = -29
# print("The absolute value of", integer, "is", abs(integer))
# # for x in range(3):
# #     print(x)          
# # print("Hello, World!")    

# print("hello")

# num = [1,2,4,6,11,20]
# seq = 0
# for val in num:
#     seq = val*val
#     print(seq)  

for i in range (1,6):
    for j in range(0,i):
        print(i, end="")
    print()
# num = list(range(0,41,5))
# print(num)