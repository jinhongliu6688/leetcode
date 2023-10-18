# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None

        a = ListNode()
        start = a
        
        while list1 and list2:
            if list1.val < list2.val:
                a.next = list1
                list1 = list1.next
            else:
                a.next = list2
                list2 = list2.next
            a = a.next

        if list1: a.next = list1
        if list2: a.next = list2

        return start.next
