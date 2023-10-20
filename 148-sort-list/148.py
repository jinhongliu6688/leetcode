# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        map = defaultdict(list) 
        while head:
            map[head.val].append(head)
            head = head.next
        
        sorted_list = sorted(map.keys())
        node = ListNode()
        start = node

        for val in sorted_list:
            for n in map[val]:
                node.next = n
                node = node.next
        node.next = None

        return start.next
