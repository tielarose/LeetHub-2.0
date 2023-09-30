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

            num_of_good_nodes = left + right
            
            if node.val >= curr_max:
                num_of_good_nodes += 1

            return num_of_good_nodes


        return dfs(root, float("-inf"))

        