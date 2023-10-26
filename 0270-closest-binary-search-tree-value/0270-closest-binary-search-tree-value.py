# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        stack = []
        prev_val = float("-inf")

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if prev_val <= target < root.val:
                return min(prev_val, root.val, key = lambda x: abs(target - x))

            prev_val = root.val
            root = root.right

        return prev_val