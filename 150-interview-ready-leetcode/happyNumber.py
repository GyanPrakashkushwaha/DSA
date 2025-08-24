class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()
        total = n
        while total not in hashSet:
            newTotal = total
            localTotal = 0
            while newTotal % 10:
                localTotal += (newTotal % 10)**2
                newTotal //= newTotal
            
            total = newTotal
            hashSet.add(newTotal)
            if newTotal == 1:
                return True
        
        return False
    
soln = Solution()
print(soln.isHappy(19))