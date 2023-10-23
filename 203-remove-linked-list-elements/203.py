# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        queue = []
        while head:
            if head.val != val:
                queue.append(head)
            head = head.next
        
        node = ListNode()
        start = node
        while queue:
            node.next = queue.pop(0)
            node = node.next
        node.next = None

        return start.next

  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        node = ListNode()
        start = node
        while head:
            if head.val != val:
                node.next = head
                node = node.next
            head = head.next
        node.next = None

        return start.next
