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


        made = {}

        root = head

        while root:
            made[root] = Node(root.val)
            root = root.next

        root = head

        while root:
            made[root].next = made.get(root.next)
            made[root].random = made.get(root.random)
            root = root.next
        
        return made.get(head)

        

        
        