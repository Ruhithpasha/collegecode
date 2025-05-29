def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
         return i
    return -1

arr=[2,3,1,6,4,5]
target = 6
index = linear_search(arr,target)
print("linear search", index)