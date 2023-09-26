# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1
        # find the middle of the linked list using a fast and slow pointer
        # ex: if the list was [1,2,3,4,5,6], find 4
        prev = None
        fast = slow = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is now the middle of the linked list (4 in my example)
        # prev is now the last node of the unreversed part of the list (3 in my example)

        # Step 2
        # reverse the linked list from the middle 
        # ex: [1,2,3,6,5,4]
        last_node = prev # save to link the reversed part of the list with the unreversed part of the list (ie so [1,2,3] can be linked with [6,5,4])

        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        last_node.next = prev

        # the second-half of the linked list is now reversed
        # "prev" is at the middle node (now 6)

        # Step 3
        # loop through the list with one pointer at the beginning, one starting from the second-half (aka "prev"). Find the max sume of these pairs

        max_sum = 0
        first = head
        second = prev

        while second:
            max_sum = max(first.val + second.val, max_sum)
            first = first.next
            second = second.next

        return max_sum

        