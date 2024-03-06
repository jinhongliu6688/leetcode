# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        node = ListNode()
        start = node
        current_val = 101

        while head:
            if head.val != current_val:
                node.next = head
                node = node.next
                current_val = head.val
            head = head.next
        node.next = None

        return start.next
