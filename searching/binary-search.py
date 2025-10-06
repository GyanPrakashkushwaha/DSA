def binarySearch(lst, tar):
    l, h = 0, len(lst)-1
    
    while l <= h:
        mid = l + (h-l)//2
        if lst[mid] == tar:
            return mid
        if lst[mid] < tar:
            l = mid+1
        else:
            h = mid-1
    
    return -1
        

def bs(lst, tar, l, h):
    if l > h:
        return -1
    
    mid = l + (h-l)//2
    if lst[mid] == tar:
        return mid
    if lst[mid] < tar:
        return bs(lst, tar, mid+1, h)
    else:
        return bs(lst, tar, l, mid-1)

        
    
    
    
    
def myBinarySearch(arr, target):
    start, end = 0, len(arr)-1
    
    while start <= end:
        mid =  start + (end -start)//2 # (start + end)//2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
        
    return -1






def reviseBinarySearch(arr, tar):
    low, high = 0, len(arr)-1
    
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            low = mid+1
        else:
            high = mid-1
    
    return -1 # Otherwise...

