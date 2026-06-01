class Solution:
    def missingNum(self, arr):
        sums=sum(arr)
        n=len(arr)+1
        index_sum=(n*(n+1))//2
        return index_sum-sums
        
        