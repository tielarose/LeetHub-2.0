# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next
        prev = None
        node_A = head

        cycle = 1

        while node_A and node_A.next:
            node_B = node_A.next
            node_C = node_B.next

            if prev:
                prev.next = node_B

            node_B.next = node_A
            node_A.next = node_C

            prev = node_A
            node_A = node_C

        return new_head

        