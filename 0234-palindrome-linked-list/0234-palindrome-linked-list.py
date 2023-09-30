# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast, prev, curr = head, head, None, head

        # reverse the first half of the linked list
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            curr.next, prev, curr = prev, curr, slow

        # if fast is not None, then the number of nodes is odd
        # we can ignore the middle (unpaird) node
        if fast:
            curr = curr.next

        # compare the two halves of the linked list
        first = prev
        second = curr
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
        