from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1
        r = sorted(m, key=lambda x: m[x])
        return r[-1]


s = Solution()
s.majorityElement([3, 2, 3])
