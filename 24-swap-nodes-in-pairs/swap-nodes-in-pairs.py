# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2, prev = None, None, None
        if curr1:= head: 
            if curr2:= curr1.next:
                head = curr2
        while curr1 and curr2:
            next_1 = curr2.next
            curr2.next = curr1
            curr1.next = next_1
            if prev:
                prev.next = curr2
            prev = curr1
            if curr1:= next_1: 
                curr2 = curr1.next
        return head
            
