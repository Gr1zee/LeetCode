from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        p1 = 0
        p2 = n
        while p1 < n or p2 < len(nums):
            res.append(nums[p1])
            res.append(nums[p2])
            p1 += 1
            p2 += 1
        return res

s = Solution()
print(s.shuffle([1, 1, 2, 2], 2))