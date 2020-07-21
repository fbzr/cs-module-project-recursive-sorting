# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if end < start:
        return -1
    
    middle = start + ((end-start)//2)

    if target == arr[middle]:
        return middle
    else:
        if target < arr[middle]:
            return binary_search(arr, target, start, middle-1)
        else:
            return binary_search(arr, target, middle+1, end)    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target, prevIndexes=0):
    # Your code here
    if not arr or (len(arr) == 1 and arr[0] != target):
        return -1

    ascending = arr[0] < arr[len(arr)-1]
    
    middle = len(arr)//2

    if target == arr[middle]:
        return middle+prevIndexes
    else:
        if (ascending and target < arr[middle]) or (not ascending and target > arr[middle]):
            return agnostic_binary_search(arr[:middle], target, prevIndexes)
        else:
            return agnostic_binary_search(arr[middle+1:], target, prevIndexes+middle+1)
