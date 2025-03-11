from collections import deque

# Определение узла бинарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # Очередь для обхода обоих деревьев
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
    
    # Если очередь пуста и все узлы совпали, деревья идентичны
    return True

# Пример использования
if __name__ == "__main__":
    # Tree 1: [1, 2, 3]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    
    # Tree 2: [1, 2, 3]
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    
    print(isSameTree(p, q))  # Output: True
    
    # Tree 3: [1, 2]
    r = TreeNode(1)
    r.left = TreeNode(2)
    
    # Tree 4: [1, None, 2]
    s = TreeNode(1)
    s.right = TreeNode(2)
    
    print(isSameTree(r, s))  # Output: False