# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        prev_less, prev = None, None
        while curr != None:
            if curr.val < x:
                if prev and prev_less:
                    if prev == prev_less:
                        prev, prev_less = curr, curr
                        curr = curr.next
                        continue
                    prev.next = curr.next
                    curr.next = prev_less.next
                    prev_less.next = curr
                    prev_less = curr
                    curr = prev.next
                elif prev:
                    prev.next = curr.next
                    curr.next = head
                    head = curr
                    prev_less = curr
                    curr = prev.next
                else:
                    prev_less, prev = curr, curr
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head
                    
