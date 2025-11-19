from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = nums + nums
        print(res)

s = Solution()
s.getConcatenation([1, 2, 3])