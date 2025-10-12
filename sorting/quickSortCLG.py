def quicksort(L, lower, upper):
    if lower < upper:
        pivot_pos = partition(L, lower, upper)
        quicksort(L, lower, pivot_pos - 1)
        quicksort(L, pivot_pos + 1, upper)
    return L

def partition(L, lower, upper):
    pivot = L[lower]
    i = lower
    for j in range(lower + 1, upper + 1):
        if L[j] <= pivot:
            i = i + 1
            L[i], L[j] = L[j], L[i]
    L[lower], L[i] = L[i], L[lower]
    print(L)
    return i


# Example usage
arr = [5, 6, 2, 1, 4, 8, 7]
sorted_arr = quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", sorted_arr)

