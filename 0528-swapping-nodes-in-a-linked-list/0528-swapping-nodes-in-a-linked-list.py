# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # find the node k nodes from the beginning
        before_A = dummy
        node_A = head

        for i in range(1,k):
            before_A = before_A.next
            node_A = node_A.next

        after_A = node_A.next

        # find the node k nodes from the end
        before_B = dummy
        node_B = head
        fast = node_A

        while fast and fast.next:
            before_B = before_B.next
            node_B = node_B.next
            fast = fast.next

        after_B = node_B.next

        # switch the pointers
        # check edge case where the two nodes to be switched are next to each other
        if after_A == node_B:
            before_A.next = node_B
            node_B.next = node_A
            node_A.next = after_B
        elif after_B == node_A:
            before_B.next = node_A
            node_A.next = node_B
            node_B.next = after_A
        else:
            before_A.next = node_B
            node_B.next = after_A
            before_B.next = node_A
            node_A.next = after_B

        return dummy.next



        
        