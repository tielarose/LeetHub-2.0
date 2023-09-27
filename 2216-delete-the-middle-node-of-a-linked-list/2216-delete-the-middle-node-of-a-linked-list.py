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

        slow, fast = head, head.next.next

        # when fast reaches the end, slow will be at the node BEFORE the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # "delete" the middle node by pointing slow to the node after the middle node
        slow.next = slow.next.next

        return head
        