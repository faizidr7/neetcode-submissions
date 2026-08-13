# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        fast = dummy
        slow = dummy

        for i in range(n):
            fast = fast.next
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # [1 2 3 4] n = 2
        # fast = 3
        # advance slow and fast pointers forward
        # slow = 1, fast = 3
        # set slow.next = slow.next.next 1 -> 4

        slow.next = slow.next.next
        return dummy.next
        
        

        

        
        