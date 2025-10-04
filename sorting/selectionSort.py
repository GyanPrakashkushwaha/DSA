
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