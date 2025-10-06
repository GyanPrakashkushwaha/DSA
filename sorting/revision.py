def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIdx = i
        for j in range(i+1, n):
            if arr[minIdx] > arr[j]:
                minIdx = j
        
        arr[minIdx], arr[i] = arr[i], arr[minIdx]
    
    return arr
print(selectionSort([10, 8,9, 63423, 1,0 , -10]))



def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key
        
    return arr
print(insertionSort([10, 8,9, 63423, 1,0 , -10]))



