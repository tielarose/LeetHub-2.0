# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast, prev, curr = head, head, None, head
        max_sum = 0

        # reverse the first half of the linked list
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            curr.next, prev, curr = prev, curr, slow

        # sum the pairs of nodes to find the max
        while slow:
            max_sum = max(max_sum, prev.val + slow.val)
            slow, prev = slow.next, prev.next

        return max_sum

# [1,2,3,4]

# slow = 1
# fast = 1
# (fast.next = 2)
# prev = 1
# curr = 2
# max_sum = 0
            




        