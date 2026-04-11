class Solution:
    def nse(self,arr):
        n=len(arr)
        res=[n]*n
        stack=[]
        for i in range (n-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if not stack :
                res[i]=n
            else:
                res[i]=stack[-1]
            stack.append(i)
        return res
    def pse(self,arr):
        n=len(arr)
        res=[-1]*n
        stack=[]
        for i in range (n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if not stack :
                res[i]=-1
            else:
                res[i]=stack[-1]
            stack.append(i)
        return res
    def sumSubMins(self, arr):
        total=0
        mod = 10**9 +7
        psee = self.pse(arr)
        nsee = self.nse(arr)
        n=len(arr)
        for i in range (n):
            left=i-psee[i]
            right=nsee[i]-i
            freq=(left*right)%mod
            value=(freq*arr[i])%mod
            total=(total+value)%mod
        return total
            
        