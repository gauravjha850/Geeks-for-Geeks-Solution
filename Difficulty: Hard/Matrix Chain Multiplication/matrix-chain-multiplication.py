class Solution:
    def matrixMultiplication(self, arr):
        n=len(arr)
        dp=[[-1]*n for _ in range (n)]
        return self.solve(arr,1,n-1,dp)
        
    def solve(self,arr,i,j,dp):
        if i==j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        min_cost=float("inf")
        
        for k in range (i,j):
            cost1=self.solve(arr,i,k,dp)
            cost2=self.solve(arr,k+1,j,dp)
            total_cost=arr[i-1]*arr[k]*arr[j]+cost1+cost2
            min_cost=min(total_cost,min_cost)
        dp[i][j]=min_cost
        return dp[i][j]
        
        