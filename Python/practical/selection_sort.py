# 5. Create a python program to sort a list of numbers using selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the minimum is at index i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update index of minimum element
        # Swap the found minimum with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
if __name__ == "__main__":
    numbers = [64, 25, 12, 22, 11]
    print("Original list:", numbers)
    
    selection_sort(numbers)
    
    print("Sorted list:", numbers)