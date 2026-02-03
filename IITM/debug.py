# def fn(n):
#     if n <= 1:
#         return 0
#     if n%2 == 0:
#         return fn(n//2)
#     else:
#         return 1+fn(n//2) + fn(n//2)
    
# fn(18)


def reverse(L):
    if len(L) <= 1:
        return L
    return [L[-1]] + reverse(L[:-1])

l2= reverse([1, 2, 3, 4, 5])
print(l2)