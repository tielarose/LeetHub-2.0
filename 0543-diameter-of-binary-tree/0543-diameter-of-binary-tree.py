# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs_longest_path(node):
            if not node:
                return 0

            left_path = dfs_longest_path(node.left)
            right_path = dfs_longest_path(node.right)

            self.diameter = max(self.diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        dfs_longest_path(root)

        return self.diameter
            




        