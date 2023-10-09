# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        deepest_level_sum = 0

        while queue:
            row_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()

                row_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            deepest_level_sum = row_sum

        return deepest_level_sum
        