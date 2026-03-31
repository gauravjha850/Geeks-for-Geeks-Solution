"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        new_node=self.reverseList(head.next)
        front=head.next
        front.next=head
        head.next=None
        return new_node
        