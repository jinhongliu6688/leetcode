# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(m + n), where m and n are the lengths of the two linked lists respectively.
# space: O(1)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize a dummy node and two pointers. p is for connecting the linked lists, and s is for later return convenience.
        s = p = ListNode()
        
        # use h1 to represent the current node of linked list 1 
        h1 = list1

        # use h2 to represent the current node of linkde list 2
        h2 = list2

        # while h1 is not null and h2 is not null
        while h1 and h2:
            # if the value of h1 is less than the value of h2
            if h1.val < h2.val:
                # connect p with h1
                p.next = h1
                # move h1 to the next node
                h1 = h1.next
            else:
                # connect p with h2
                p.next = h2
                # move h2 to the next node
                h2 = h2.next
            # move p to the next node
            p = p.next

        # the above while loop will terminate if one of the h1 and h2 is null
        # Check if there are remaining nodes in list1 or list2
        # Attach the remaining nodes in list1 to the merged list
        if h1:
            p.next = h1
        # Attach the remaining nodes in list2 to the merged list
        elif h2:
            p.next = h2
        
        # s points to the dummy node with value 0, don't return s. The first node of the answer is the next one of the dummy node.
        return s.next
