n = int(input("Enter the number of elements in the array: "))
arr = [0] *n  # Initialize the array with a fixed size
for i in range(n):
    arr[i] = int(input(f"Enter the number for index {i}: "))  # Assign values directly
print(arr)

total = 0
for num in arr:
    total += num
print(f"The sum of the array is: {total}")