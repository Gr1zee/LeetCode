from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        counter = 0
        f = False
        for n in nums:
            if n == 1 and f:
                counter += 1
            elif n == 1 and (not f):
                f = True
                counter = 1
            else:
                res = max(res, counter)
                counter = 0
                f = False
        res = max(res, counter)
        return res
            
s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))