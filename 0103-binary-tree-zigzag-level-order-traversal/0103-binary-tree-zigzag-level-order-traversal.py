# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []
        left_to_right = True

        while queue:
            next_level_queue = deque()
            curr_level_traversal = []

            for _ in range(len(queue)):
                node = queue.popleft()

                curr_level_traversal.append(node.val)

                if left_to_right:
                    if node.left:
                        next_level_queue.appendleft(node.left)
                    if node.right:
                        next_level_queue.appendleft(node.right)
                else:
                    if node.right:
                        next_level_queue.appendleft(node.right)
                    if node.left:
                        next_level_queue.appendleft(node.left)

            result.append(curr_level_traversal)
            left_to_right = not left_to_right
            queue = next_level_queue

        return result