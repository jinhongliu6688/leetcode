# Method 1
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

# Method 2
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
        skip_val = -101

        while head:
            if ((head.next and head.val != head.next.val) or not head.next) and head.val != skip_val:
                node.next = head
                node = node.next
            else:
                skip_val = head.val
            head = head.next
        node.next = None
        
        return start.next
