# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = []

        def find(node, max_val):
            if node is None:
                return None

            if node.val >= max_val:
                self.result.append(node.val)
                

            current_max_val = max(max_val, node.val)
            find(node.left, current_max_val)
            find(node.right, current_max_val)

        find(root, float('-inf'))
        print(self.result)

        return len(self.result)
