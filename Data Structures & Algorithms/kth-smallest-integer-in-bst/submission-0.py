# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.seen = []

        def go(node):
            if node is None:
                return None

            self.seen.append(node.val)

            go(node.left)
            go(node.right)

        go(root)
        # print(self.seen)
        self.seen.sort()

        return self.seen[k-1]
        