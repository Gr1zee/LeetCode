from preloaded import Node

# Node is defined in preloaded:
# class Node:
#     def __init__(self, data):
#        self.data = data
#        self.next = None


def length(node: Node) -> int:
    curr = Node
    l = 0
    while curr:
        l += 1
        curr = curr.next
    return l


def count(node: Node, data) -> int:
    curr = Node
    c = 0
    while curr:
        if curr.data == data:
            c += 1
        curr = curr.next
    return c
