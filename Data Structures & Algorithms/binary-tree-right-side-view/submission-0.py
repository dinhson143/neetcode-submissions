# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.seen = {}

        def find(node, level):
            if node is None:
                return None

            if self.seen.get(level, None) is None:
                self.seen[level] = node.val
            
            current_lv = level + 1
            find(node.right, current_lv)
            find(node.left, current_lv)

        find(root, 0)
        result = [val for val in self.seen.values()]
        # print(self.seen)

        return result

        