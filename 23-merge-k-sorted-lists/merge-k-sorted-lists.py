# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Memory Efficient Solution
        '''
        def mergeTwoLists(list1, list2):
            if not list1 or not list2:
                if not list1 and list2:
                    return list2
                elif not list2 and list1:
                    return list1
                else:
                    return None

            prev, head = None, None
            i = 1
            while list1 and list2:
                if list1.val > list2.val:
                    new = list2
                    if prev:
                        prev.next = new
                    prev = new
                    list2 = list2.next
                    if i:
                        head = prev
                else:
                    new = list1
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
        
        curr = None
        if lists:
            curr = lists[0]
        for i in range(1,len(lists)):
            curr = mergeTwoLists(curr, lists[i])
        return curr
        '''
        #Heap using solution, Time efficient
        head = ListNode(None)
        curr = head
        heap = []
        count =0

        for i in range(len(lists)):
            if lists[i]:
                #Use Node as heap's value
                heapq.heappush(heap, (lists[i].val, count, lists[i]))
                count += 1

        while heap:
            val, ien, node = heapq.heappop(heap)
            next_node = node.next
            if next_node:
                heapq.heappush(heap,(next_node.val,count,next_node))
                count += 1
            curr.next = node
            curr = node

        return head.next
