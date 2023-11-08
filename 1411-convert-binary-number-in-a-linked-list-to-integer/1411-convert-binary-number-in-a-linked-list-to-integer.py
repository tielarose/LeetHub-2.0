# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        digits_list = []

        while head:
            digits_list.append(str(head.val))
            head = head.next

        return int("".join(digits_list), 2)
        