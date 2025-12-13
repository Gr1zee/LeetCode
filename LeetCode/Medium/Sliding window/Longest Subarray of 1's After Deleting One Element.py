from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        res = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                while zeros != 0:
                    if nums[left] == 0:
                        zeros -= 1
                    left += 1
                zeros += 1
            res = max(right - left, res)
        return res
