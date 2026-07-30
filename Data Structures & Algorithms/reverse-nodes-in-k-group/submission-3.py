# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        arr = []

        def checkk(node, k):
            while k > 0:
                if node is None:
                    return False
                k -= 1
                node = node.next
            
            return True

        while current:
            node = current
            if checkk(node, k):
                temp = []
                for i in range(0, k):
                    # print(current.val)
                    new_node = ListNode(current.val)
                    temp.append(new_node)
                    current = current.next
                temp = temp[::-1]
                arr.extend(temp)
                continue

            arr.append(current)
            current = current.next


        temp = None
        result = None
        for node in arr:
            #  print(node.val)
            if temp is None:
                temp = node
                result = temp
            else:
                temp.next = node
                temp = node

        return result

            
                


             

        