def fn(n):
    if n <= 1:
        return 0
    if n%2 == 0:
        return fn(n//2)
    else:
        return 1+fn(n//2) + fn(n//2)
    
fn(18)