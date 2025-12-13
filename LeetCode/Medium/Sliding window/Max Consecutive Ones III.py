from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        zeros = 0
        for right in range(0, len(nums)):
            if nums[right] == 0:
                while zeros >= k:
                    if nums[left] == 0:
                        zeros -= 1
                    left += 1
                zeros += 1
            res = max(right - left + 1, res)
        return res


s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
