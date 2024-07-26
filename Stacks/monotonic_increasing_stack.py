def monotic_stack(nums):
    stack = []
    result = []
    
    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        
        stack.append(num)
    
    while stack:
        result.insert(0,stack.pop())
    
    