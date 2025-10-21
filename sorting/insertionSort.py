def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

print(insertionSort([9, 15, 7, 3, 12, 5, 2]))

# count = 0
def standardSelectionSort(arr):
    count = 0
    # The loop runs n-1 times
    for i in range(len(arr) - 1):
        smallest_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_idx]:
                smallest_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[smallest_idx] = arr[smallest_idx], arr[i]
        count += 1
        
    return arr, count

print(standardSelectionSort([64, 25, 22, 12, 11, 3]))



# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         j = i -1
#         key = arr[i]
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
    
#     return arr

# def selectionSort(arr):
#     for i in range(0, len(arr)):
#         smallest = i

#         for j in range(i+1, len(arr)):
#             if arr[smallest] > arr[j]:
#                 smallest = j
        
#         arr[smallest], arr[i] = arr[i], arr[smallest]
    
#     return arr