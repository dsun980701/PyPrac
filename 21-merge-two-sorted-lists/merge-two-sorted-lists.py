# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            if not list1 and list2:
                return list2
            elif not list2 and list1:
                return list1
            else:
                return None

        prev, head = None, None
        i = 1
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                new = ListNode(list2.val)
                if prev:
                    prev.next = new
                prev = new
                list2 = list2.next
                if i:
                    head = prev
            else:
                new = ListNode(list1.val)
                if prev:
                    prev.next = new
                prev = new
                list1 = list1.next
                if i:
                    head = prev
            i = 0
            
        if list1 != None:
            prev.next = list1
            return head
        elif list2 != None:
            prev.next = list2
            return head
        else:
            return head
