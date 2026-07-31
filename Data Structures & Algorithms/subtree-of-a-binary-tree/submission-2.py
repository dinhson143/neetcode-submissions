# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(rootNode, subNode):
            if rootNode is None and subNode is None:
                return True

            if rootNode is None or subNode is None:
                return False 

            if rootNode.val != subNode.val:
                return False

            return check(rootNode.left, subNode.left) and check(rootNode.right, subNode.right)

        if root is None:
            return False

        if check(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)