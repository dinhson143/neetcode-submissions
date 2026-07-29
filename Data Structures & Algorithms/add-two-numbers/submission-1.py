# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dem = 1
        n1 = 0
        n2 = 0
        while l1:
            n1 += l1.val * dem 
            dem *= 10
            l1 = l1.next

        dem = 1
        while l2:
            n2 += l2.val * dem 
            dem *= 10
            l2 = l2.next

        result = str(n1+n2)
        current = None
        for n in result:
            temp = ListNode(val=int(n), next=current)
            current = temp
        
        return current
