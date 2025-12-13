from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or k <= 0 or k > len(nums):
            return 0
        window_sum = sum(nums[:k]) / k
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += (nums[i] - nums[i - k]) / k
            max_sum = max(window_sum, max_sum)
        return max_sum
