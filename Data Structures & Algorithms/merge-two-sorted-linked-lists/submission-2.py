# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr1 = list1
        curr2 = list2
        head = None
        while curr1 or curr2:
            if (curr1 and curr2):
                if curr1.val < curr2.val:
                    curr = curr1
                    curr1 = curr1.next
                elif curr2:
                    curr = curr2
                    curr2 = curr2.next
            elif curr1:
                curr = curr1
                curr1 = curr1.next
            elif curr2:
                curr = curr2
                curr2 = curr2.next
            
            if prev:
                prev.next = curr
            else:
                head = curr

            prev = curr

        return head