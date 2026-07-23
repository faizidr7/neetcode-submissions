# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        prev = None
        slow.next = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        l1 = head
        l2 = prev
        while l2 is not None:
            next1 = l1.next
            next2 = l2.next

            l1.next = l2
            l2.next = next1
            l1 = next1
            l2 = next2
        
        






        