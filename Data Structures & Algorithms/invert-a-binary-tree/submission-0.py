# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        head = TreeNode(root.val)
        def invert(node, head):
            if node is None:
                return None

            if node.left:
                node_left = TreeNode(node.left.val)
                head.right = node_left
                print(f"left: {head.right.val, node.val}")

            if node.right:
                node_right = TreeNode(node.right.val)
                head.left = node_right
                print(f"right: {head.left.val, node.val, node.right.val}")
            
            invert(node.left, head.right)
            invert(node.right, head.left)

        invert(root, head)
        return head