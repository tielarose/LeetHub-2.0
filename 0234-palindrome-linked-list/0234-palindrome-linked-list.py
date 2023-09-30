# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front_pointer = head

        def recursively_check(curr_node):
            if curr_node:
                if not recursively_check(curr_node.next):
                    return False
                if self.front_pointer.val != curr_node.val:
                    return False
                self.front_pointer = self.front_pointer.next

            return True

        return recursively_check(head)