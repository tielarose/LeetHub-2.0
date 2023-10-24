# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf_value_sequence(root):
            result = []
            stack = [root]

            while stack:
                curr_node = stack.pop()
                if curr_node.right:
                    stack.append(curr_node.right)
                if curr_node.left:
                    stack.append(curr_node.left)
                if not curr_node.left and not curr_node.right:
                    result.append(curr_node.val)

            return result

        return leaf_value_sequence(root1) == leaf_value_sequence(root2)


        