# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs_validate(node, lower_bound, upper_bound):
            if not node:
                return True

            if not (lower_bound < node.val < upper_bound):
                return False

            left = dfs_validate(node.left, lower_bound, node.val)
            right = dfs_validate(node.right, node.val, upper_bound)

            return left and right

        return dfs_validate(root, float("-inf"), float("inf"))
        