# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return None
        
        queue = []
        seen_val = set()

        while head:
            if head.val not in seen_val:
                queue.append(head)
                seen_val.add(head.val)
            elif head.val in seen_val:
                if queue and queue[-1].val == head.val:
                    queue.pop()
            head = head.next

        node = ListNode()
        start = node

        while queue:
            node.next = queue.pop(0)
            node = node.next
        node.next = None

        return start.next
