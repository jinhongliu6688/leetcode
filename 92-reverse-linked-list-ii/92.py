# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = []
        queue_1 = []
        queue_2 = []
        n = 1
        while head:
            if n < left:
                queue_1.append(head)
            elif right >= n >= left:
                stack.append(head)
            elif n > right:
                queue_2.append(head)
            head = head.next
            n += 1
        
        node = ListNode()
        start = node
        while queue_1:
            node.next = queue_1.pop(0)
            node = node.next
        while stack:
            node.next = stack.pop()
            node = node.next
        while queue_2:
            node.next = queue_2.pop(0)
            node = node.next
        node.next = None
        
        return start.next
