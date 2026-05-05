'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    
    def meeting_(self,meetingpoint):
        length=1
        temp=meetingpoint
        while temp.next!=meetingpoint:
            length=length+1
            temp=temp.next
        return length
        
    
    
    
    
    def lengthOfLoop(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if fast== slow:
                
                return self.meeting_(slow)
        return 0