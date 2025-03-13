from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        q = deque()
        q.append(root)
        while q:
            tmp_lvl = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp_lvl.append(node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(tmp_lvl)
        return res

s = Solution()  
print(Solution.levelOrder(root=[3,9,20, None, None,15,7]))