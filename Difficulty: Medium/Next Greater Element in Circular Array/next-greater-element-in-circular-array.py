class Solution:
    def nextGreater(self, arr):
        n=len(arr)
        res=[-1]*n
        stack=[]
        for i in range (2*n-1,-1,-1):
            while stack and stack[-1] <= arr[i%n] :
                stack.pop()
            if not stack :
                res[i%n]=-1
            else:
                res[i%n]=stack[-1]
            stack.append(arr[i%n])
        return res