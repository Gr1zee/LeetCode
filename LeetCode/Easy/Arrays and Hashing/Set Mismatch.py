from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums)):
            if i+1 != nums[i]:
                res.append(nums[i])
                res.append(i+1)
                return res