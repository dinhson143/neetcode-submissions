# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        arr = []

        while temp:
            arr.append(temp)
            temp = temp.next

        des = len(arr) - n - 1
        if des < 0:
            return head.next
        arr[des].next = arr[des].next.next

        return head

