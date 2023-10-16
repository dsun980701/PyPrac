# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        last_node = head
        num_nodes = 1
        # Get linked list length
        while last_node.next != None:
            num_nodes += 1
            last_node = last_node.next
        k = k % num_nodes
        if k == 0:
            return head
        # Make a circular linked list
        last_node.next = head
        for _ in range(num_nodes - k - 1):
            head = head.next
        # Detach
        result = head.next
        head.next = None
        return result
