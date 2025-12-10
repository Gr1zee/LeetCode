from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        h = 0
        max_water = 0
        max_water = max(max_water, h * r - l)
        while r > l:
            if height[l] > height[r]:
                h = height[r]
                r -= 1
            else:
                h = height[l]
                l += 1
            max_water = max(max_water, h * r - l)
        return max_water
