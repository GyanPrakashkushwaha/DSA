from turtle import right


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    sorted_left = merge_sort(arr[:mid])
    sorted_right = merge_sort(arr[mid:])
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from left or right
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example usage:
if __name__ == "__main__":
    my_list = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original list: {my_list}")
    sorted_list = merge_sort(my_list)
    print(f"Sorted list: {sorted_list}")

    my_list_2 = [12, 11, 13, 5, 6, 7]
    print(f"Original list: {my_list_2}")
    sorted_list_2 = merge_sort(my_list_2)
    print(f"Sorted list: {sorted_list_2}")
    



def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    left = mergeSort(leftHalf)
    right = mergeSort(rightHalf)

    return merge(left, right)

def merge(left, right):
    res = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            
    res.extend(left[i:])
    res.extend(right[j:])
    
    return res