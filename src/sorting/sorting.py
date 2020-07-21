# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    indexA = 0
    indexB = 0
    while indexA < len(arrA) and indexB < len(arrB):
        if arrA[indexA] < arrB[indexB]:
            merged_arr[indexA + indexB] = arrA[indexA]
            indexA += 1
        else:
            merged_arr[indexA + indexB] = arrB[indexB]
            indexB += 1

    while indexA < len(arrA):
        merged_arr[indexA + indexB] = arrA[indexA]
        indexA += 1
    while indexB < len(arrB):
        merged_arr[indexA + indexB] = arrB[indexB]
        indexB += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    # split arr
    middle = len(arr)//2
    
    # invoke merge_sort in the first and second half
    arrA = merge_sort(arr[:middle])
    arrB = merge_sort(arr[middle:])
    
    # return merged sorted arrays
    return merge(arrA, arrB)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

