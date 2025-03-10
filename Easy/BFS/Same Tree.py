from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q_q = deque()
        q_p = deque()
        q_p += p
        q_q += q
        while q_q and q_p:
            for _ in range(len(q_q)):
                node = q_q.popleft()
                node2 = q_p.popleft()
                if node != node2:
                    return False
                i
        