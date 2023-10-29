# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev_num = None
        while curr and curr.next != None:
            # Curr's next is not a duplicate
            if curr.next.val != curr.val:
                prev_num = curr
                curr = curr.next
            # Curr's next is a duplicate
            else:
                val = curr.val
                # Traverse the linked list until there is no more duplicate, or the list ends
                while curr != None and curr.val == val:
                    curr = curr.next
                #if prev_num existed
                if prev_num:
                    prev_num.next = curr
                # prev_num didn't exist
                else:
                    head = curr
        return head