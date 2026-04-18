'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        dummy=Node(0)
        dummy.next=head
        temp=dummy
        count=1
        while temp.next is not None  :
            if count==x:
                temp.next=temp.next.next
                break
            else:
                temp=temp.next
                count+=1
        return dummy.next
