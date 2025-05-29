# 4. Create a python program to implement binary search algorithm.
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
            
    return -1  # Target not found

# Example usage
if __name__ == "__main__":
    sorted_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    target_value = int(input("Enter the number to search: "))
    
    result = binary_search(sorted_list, target_value)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")
