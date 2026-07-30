# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def find(node):
            if node is None:
                return 0
            
            current_left_length = find(node.left)
            current_right_length = find(node.right)
            self.result = max(current_left_length + current_right_length, self.result)

            return max(current_left_length,current_right_length) + 1
        find(root)
        return self.result