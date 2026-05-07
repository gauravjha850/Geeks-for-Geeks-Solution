'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def buildTree(self, inorder, preorder):
        inorder_map={val: i for i,val in enumerate(inorder)}
        self.pre_idx=0
        def helper(in_left,in_right):
            if in_left > in_right:
                return None
            root_value=preorder[self.pre_idx]
            root=Node(root_value)
            mid=inorder_map[root_value]
            self.pre_idx +=1
            root.left=helper(in_left,mid-1)
            root.right=helper(mid+1,in_right)
            return root
        return helper(0,len(preorder)-1)
        
        