# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr_max):
            if not node:
                return 0

            left = dfs(node.left, max(curr_max, node.val))
            right = dfs(node.right, max(curr_max, node.val))
            
            if node.val >= curr_max:
                return left + right + 1
            else:
                return left + right

        return dfs(root, root.val)

        