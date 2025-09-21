def oneTon(n):
    # Base Case
    if n == 0:
        return
    oneTon(n-1)
    print(n)
    
oneTon(5)