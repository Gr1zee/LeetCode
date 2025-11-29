# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        c = 0
        while curr:
            curr = curr.next
            c += 1
        mid = c // 2 + 1
        count = 1
        while curr:
            if count == mid:
                return curr
            curr = curr.next
            count += 1
