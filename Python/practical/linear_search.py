# 3. Create a python program to implement linear search on array.

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# Example usage
if __name__ == "__main__":
    # Sample array
    arr = [10, 25, 30, 45, 50, 60]
    
    # Input from user
    target = int(input("Enter the element to search: "))
    
    # Perform search
    result = linear_search(arr, target)
    
    # Output result
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")