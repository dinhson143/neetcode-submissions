# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float("-inf")

        def find(node):
            if node is None:
                return 0

            left = max(0, find(node.left))
            right = max(0, find(node.right))

            current_path_sum = node.val + left + right
            self.result = max(self.result, current_path_sum)

            # print(node.val, left, right, self.result)
            return node.val + max(left, right)

        find(root)
        return self.result


