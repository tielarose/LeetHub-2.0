from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        largest_values_array = []

        while queue:
            row_max = queue[0].val

            for _ in range(len(queue)):
                node = queue.popleft()

                row_max = max(row_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            largest_values_array.append(row_max)

        return largest_values_array
        