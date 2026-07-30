# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.result = 0

        def find(node):
            if node is None:
                return 0

            current_left = find(node.left)
            current_right = find(node.right)

            self.result = max(abs(current_left - current_right), self.result)

            return max(current_left, current_right) + 1

        find(root)
        return self.result <= 1

            