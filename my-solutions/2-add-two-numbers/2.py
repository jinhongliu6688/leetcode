# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        start = l3
        ten_val = 0

        while l1 or l2:
            if l1 and l2: sum_val = l1.val + l2.val + ten_val
            elif l1: sum_val = l1.val + ten_val
            elif l2: sum_val = l2.val + ten_val

            l3.val = sum_val - 10 if sum_val >= 10 else sum_val
            ten_val = 1 if sum_val >= 10 else 0

            if l1: l1 = l1.next
            if l2: l2 = l2.next

            if l1 or l2 or ten_val == 1:
                l3.next = ListNode()
                l3 = l3.next
        
        if ten_val == 1: l3.val = 1

        return start
