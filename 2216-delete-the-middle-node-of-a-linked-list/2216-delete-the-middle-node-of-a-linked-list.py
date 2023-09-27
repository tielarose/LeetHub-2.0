# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case: list with a single node
        if not head.next:
            return None

        prev = ListNode(0)
        prev.next = head
        fast = slow = head

        # find the middle node, and keep track of the node before it with "prev"
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

        # "delete" the middle node by pointing prev to the node after the middle node
        prev.next = slow.next

        return head
        