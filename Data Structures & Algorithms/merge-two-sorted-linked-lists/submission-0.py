# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1 # attach node
                list1 = list1.next # moves list1 forward
                tail = tail.next # moves tail forward
            else:
                tail.next = list2 # attach node
                list2 = list2.next # moves list2 forward
                tail = tail.next # moves tail forward
        
        tail.next = list1 or list2
        return dummy.next 



        