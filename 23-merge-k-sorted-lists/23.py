# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list_1 = []
        
        for head in lists:
            while head:
                list_1.append(head)
                head = head.next
        
        list_1.sort(key=lambda x: x.val)

        node = ListNode()
        start = node
        while list_1:
            node.next = list_1.pop(0)
            node = node.next
        
        return start.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = ListNode()
        start = node
        not_none = len([x for x in lists if x])

        while not_none > 0:
            vals = []
            for head in lists:
                if head:
                    vals.append(head.val)

            min_val = min(vals)
            vals.clear()

            for i, head in enumerate(lists):
                if head and head.val == min_val:
                    node.next = head
                    node = node.next
                    head = head.next
                    lists[i] = head
                    if not head:
                        not_none -= 1

        return start.next
                
