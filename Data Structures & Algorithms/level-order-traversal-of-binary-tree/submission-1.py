# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = {}

        def find(node, level):
            if node is None:
                return None

            if self.result.get(level, None):
                self.result[level].append(node.val)
            else:
                self.result[level] = [node.val]
            current_lv = level + 1
            find(node.left, current_lv)
            find(node.right, current_lv)

        find(root, 0)
        # print(self.result)
        # kq = [val for val in self.result.values()]
        # print(kq)
        return [val for val in self.result.values()]

            
        