# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def find(node, current):
            if node is None:
                return None

            if node.left is None and node.right is None:
                self.result = max(self.result, current+1)
                # print(self.result)
            
            current_path = current + 1

            find(node.left, current_path)
            find(node.right, current_path)

        find(root, 0)

        return self.result

            
