# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1 = ""
        num_2 = ""

        while l1:
            num_1 += str(l1.val)
            l1 = l1.next
        
        while l2:
            num_2 += str(l2.val)
            l2 = l2.next

        sum_val = deque(list(str(int(num_1) + int(num_2))))

        node = ListNode()
        start = node
        while sum_val:
            node.next = ListNode(val = int(sum_val.popleft()))
            node = node.next
        return start.next
