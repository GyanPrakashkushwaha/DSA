def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
def partition(arr, st, end):
    pivot = arr[end]
    idx = st - 1
    comparisions = 0 
    
    for i in range(st, end):
        comparisions += 1
        if arr[i] <= pivot:
            idx += 1
            swap(arr, i, idx)
    
    idx += 1
    swap(arr, idx, end)
    return idx, comparisions

def quickSort(arr, st, end):
    if st < end:
        pvtIdx, compar = partition(arr, st, end)
        print(compar)
        quickSort(arr, st, pvtIdx-1)
        quickSort(arr, pvtIdx+1, end)
    
    return


# Example usage
arr = [10, 7, 8, 9, 1, 5]
quickSort(arr, 0, len(arr)-1)
print(arr)  # Output: [1, 5, 7, 8, 9, 10]
