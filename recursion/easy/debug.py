def fn(n):
    if n <= 1:
        return 0
    one = fn(n-1)
    two = fn(n-2)
    return one + two 

fn(4)