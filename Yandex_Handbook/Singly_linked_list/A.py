class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add(head: Node, x, y):
    current = head
    index = 0
    while current and index < x:
        current = current.next
        index += 1
    if current is None:
        return head
    new_node = Node(y)
    new_node.next = current.next
    current.next = new_node
    return head

def print_pos(head: Node, x):
    current = head
    index = 0
    while current:
        if index == x:
            print(current.data)
            return
        current = current.next
        index += 1

def delete_pos(head, x):
    if x == 0:
        return head 
    current = head
    index = 0
    while current and index < x - 1:
        current = current.next
        index += 1
    if current is None or current.next is None:
        return head
    current.next = current.next.next
    return head

q = int(input())
head = Node(None)

for _ in range(q):
    data = list(map(int, input().split()))
    if data[0] == 1:
        x, y = data[1], data[2]
        head = add(head, x, y)
    elif data[0] == 2:
        x = data[1]
        print_pos(head, x)
    elif data[0] == 3:
        x = data[1]
        head = delete_pos(head, x)