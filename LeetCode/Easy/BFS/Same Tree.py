from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            queue = deque()
            queue.append((p, q))  # Добавляем корни обоих деревьев
            while queue:
                node1, node2 = queue.popleft()  # Извлекаем узлы из очереди
                
                # Если оба узла None, пропускаем
                if not node1 and not node2:
                    continue
                
                # Если один из узлов None, а другой нет, деревья не идентичны
                if not node1 or not node2:
                    return False
                
                # Если значения узлов не равны, деревья не идентичны
                if node1.val != node2.val:
                    return False
                
                # Добавляем левых и правых потомков в очередь
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            return True
s = Solution()
print(s.isSameTree(q=TreeNode([1,2,3]), p=TreeNode([1,2,3])))