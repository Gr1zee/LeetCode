from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ind = []
        for i in range(len(nums)):
            ind.append([nums[i], i, 0])
        ind.sort()
        l = 1
        for i in range(1, len(ind)):
            if ind[i-1][0] == ind[i][0]:
                ind[i][2] = ind[i-1][2]
            else:
                ind[i][2] = l
            l += 1
        ind.sort(key=lambda x: (x[1]))
        res = []
        for n in range(len(ind)):
            res.append(ind[i][2])
        return res

s = Solution()
print(s.smallerNumbersThanCurrent([7, 7, 7, 7]))