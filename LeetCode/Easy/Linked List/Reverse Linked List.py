# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: optional[ListNode]) -> optional[ListNode]:
        if not head:
            return None
        temp = head
        tail = ListNode(val=head.val)
        while temp.next:
            temp = temp.next
            tail = ListNode(val=temp.val, next=tail)
        return tail
        