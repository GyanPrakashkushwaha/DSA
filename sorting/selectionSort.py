
def selectionSort(lst):
    n = len(lst)
    for i in range(n):
        smallest = i
        for j in range(i, n):
            if lst[smallest] > lst[j]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]
        
    return lst

print(selectionSort([6, 4, 1, 10, 3, 7]))


def selectionSort2(L):
    n = len(L)
    for i in range(n-1):
        minIdx = i
        for j in range(i+1, n):
            if L[j] < L[minIdx]:
                minIdx = j
        L[i], L[minIdx] = L[minIdx], L[i]
    
    return L
#                                  i  
print(selectionSort2([6, 4, 1, 10, 3, 7]))