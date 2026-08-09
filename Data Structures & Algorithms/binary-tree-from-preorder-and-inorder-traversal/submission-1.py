# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def construct(left_in, right_in):
            if left_in > right_in:
                return None

            temp = preorder[self.pre_idx]
            root = TreeNode(temp)         
            self.pre_idx += 1

            pivot = self.inorder_map[temp]

            root.left = construct(left_in, pivot - 1)
            root.right = construct(pivot + 1, right_in)

            return root

        return construct(0, len(preorder) - 1)


            



            
        