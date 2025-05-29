def gcd(a, b):
    while b:
        temp = a % b
        a = b
        b = temp
    return a


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))


result = gcd(n1, n2)
print(f"The GCD of {n1} and {n2} is {result}.")


