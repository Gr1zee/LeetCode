from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        index = 0
        c = 0
        while c != n - 1:
            if nums[index] == 0:
                nums.append(0)
                nums.pop(index)
            else:
                index += 1
            c += 1
        return nums
