# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.result = TreeNode(val=0)

        def find(node):
            if node is None:
                return False 

            l = find(node.left)
            r = find(node.right)
            if l and r:
                self.result = node
            if (l or r) and (node.val == p.val or node.val == q.val):
                self.result = node
            if node.val == p.val or node.val == q.val:
                return True

            return find(node.left) or find(node.right)

        find(root)
        return self.result

                
        