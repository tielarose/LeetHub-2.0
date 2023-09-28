# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # find the node k nodes from the beginning
        node_A = head

        for i in range(1,k):
            node_A = node_A.next

        # find the node k nodes from the end
        node_B = head
        fast = node_A

        while fast and fast.next:
            node_B = node_B.next
            fast = fast.next

        # switch the values
        node_B.val, node_A.val = node_A.val, node_B.val

        return dummy.next



        
        