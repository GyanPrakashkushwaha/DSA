def monotonic_increasing_stack(nums):
    stack = []
    
    for i in nums:
        while stack and stack[-1] > i:
            stack.pop()
        
        stack.append(i)
    
    return stack

print(monotonic_increasing_stack([2, 1, 2, 4, 3])) 
