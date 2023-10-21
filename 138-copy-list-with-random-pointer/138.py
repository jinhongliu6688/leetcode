"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        h1 = head
        map = {}

        while h1:
            if h1 not in map:
                map[h1] = copy.deepcopy(h1)
            if h1.next not in map:
                map[h1.next] = copy.deepcopy(h1.next)
            if h1.random not in map:
                map[h1.random] = copy.deepcopy(h1.random)
            h1 = h1.next
        
        return map[head]
