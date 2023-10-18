# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        node = ListNode()
        start = node
        
        while head:
            stack.append(head)
            head = head.next
            if len(stack) == k:
                while stack:
                    node.next = stack.pop()
                    node = node.next
        if stack:
            node.next = stack[0]
        else:
            node.next = None

        return start.next
