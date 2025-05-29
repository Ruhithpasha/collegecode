# 2. Create a python program to find the greatest number from a list of given numbers.

def find_greatest_number(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

# Example usage
numbers = [45, 12, 78, 34, 89, 23]
greatest = find_greatest_number(numbers)

if greatest is not None:
    print("The greatest number in the list is:", greatest)
else:
    print("The list is empty.")