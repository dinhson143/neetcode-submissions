# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True

        def check(nodep, nodeq):
            if nodep is None and nodeq is None:
                return None

            if (type(nodep) != type(nodeq)):
                self.result = False
                return None

            if nodep.val != nodeq.val:
                print(nodep.val, nodeq.val)
                self.result = False

            check(nodep.left, nodeq.left)
            check(nodep.right, nodeq.right)

        check(p, q)
        return self.result

        
        