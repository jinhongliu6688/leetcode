# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        queue_1 = []
        queue_2 = []

        while head:
            if head.val < x:
                queue_1.append(head)
            else:
                queue_2.append(head)
            head = head.next
        
        node = ListNode()
        start = node

        while queue_1:
            node.next = queue_1.pop(0)
            node = node.next

        while queue_2:
            node.next = queue_2.pop(0)
            node = node.next

        node.next = None
        return start.next
