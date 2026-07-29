"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        arr = {}
        current = None
        first = None
        while temp:
            node = Node(x=temp.val)
            arr[temp] = node
            if current is None:
                first = node
            else:
                current.next = node
            
            current = node
            temp = temp.next

        temp = head
        temp2 = first
        while temp:
            # temp2.random = arr[temp.random]
            if temp.random:
                temp2.random = arr[temp.random]

            # print(temp.random)
            # print(temp2.val)
            # print(temp2.random)
            temp = temp.next
            temp2 = temp2.next
            
        return first

