# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        temp = head
        run = temp.next
        while temp:
            run = run.next
            if temp.val:
                return True
            run = run.next
            temp = temp.next
        return False
