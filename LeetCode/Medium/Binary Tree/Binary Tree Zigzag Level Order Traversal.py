from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return []
        
        q = deque()
        q.append(root)
        isZig = False
        while q:
            tmp_lvl = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp_lvl.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
             
            if isZig:
                tmp_lvl.reverse()
            
            res.append(tmp_lvl)
            isZig = not isZig
        return res