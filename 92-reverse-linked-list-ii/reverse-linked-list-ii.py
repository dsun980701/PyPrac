# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        prev = None
        counter = 1
        while curr and counter != left:
            prev = curr
            curr = curr.next
            counter += 1
        # Now curr is on the node with the left, and prev is on the node before the fliping node
        if not curr:
            return head
        rev_prev = prev
        prev = curr
        curr = curr.next
        while curr and counter < right:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            counter += 1
        if not rev_prev:
            head.next = curr
            return prev
        rev_prev.next.next = curr
        curr = prev
        rev_prev.next = curr
        return head