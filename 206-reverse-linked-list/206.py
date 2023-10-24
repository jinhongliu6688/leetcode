# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        node = ListNode()
        start = node
        while stack:
            node.next = stack.pop()
            node = node.next
        node.next = None

        return start.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        node = None
        
        while head:
            h1 = head
            head = head.next
            h1.next = node
            node = h1
        
        return h1
