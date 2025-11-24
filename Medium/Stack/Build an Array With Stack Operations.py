from typing import List
from collections import deque

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        stack = []
        for i in range(1, n+1):
            if i in target:
                stack.append(i)
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")
            if stack == target:
                return res

s = Solution()
print(s.buildArray([1, 2], 4))