# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        current = None
        for l in lists:
            while l:
               arr.append(l.val)
               l = l.next
        s_arr = sorted(arr)
        for num in s_arr[::-1]:
            node = ListNode(num, current)
            current = node
        
        return current