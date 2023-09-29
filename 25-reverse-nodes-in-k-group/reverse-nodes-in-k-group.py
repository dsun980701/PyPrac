# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head
        stack = []
        curr = head
        prev = None
        initial_loop = 1
        while True:
            # Traverse through the singly linked list k times
            while len(stack) < k and curr:
                stack.append(curr)
                curr = curr.next
            # If the traversal ended prematurely, we have reached the end
            if len(stack) != k:
                if stack:
                    curr = stack[0]
                break
            while stack:
                node = stack.pop()
                if initial_loop:
                    head = node
                    prev = head
                    initial_loop = 0
                else:
                    prev.next = node
                    prev = node
        prev.next = curr
        return head
