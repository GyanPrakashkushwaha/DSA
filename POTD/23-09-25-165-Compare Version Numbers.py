class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n1, n2 = len(v1), len(v2)
        l1 = l2 = 0

        while l1 < n1 and l2 < n2:
            if int(v1[l1]) > int(v2[l2]):
                return 1
            l1 += 1
            l2 += 1
        
        while l1 < n1:
            if int(v1[l1]) > int(v2[l2]):
                return 1
            l1 += 1
        
        while l2 < n2:
            if int(v1[l1]) > int(v2[l2]):
                return 1
            l2 += 1
        
        return -1
    
version1 = "1.2"
version2 = "1.10"
Solution().compareVersion(version1, version2)


print(int('0001') == int('00000001'))
print(int('00000002'))