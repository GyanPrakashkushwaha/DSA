def n_to_1(n):
    # Base Case
    if n == 0:
        return
    n_to_1(n-1)
    print(n)
    
n_to_1(5)