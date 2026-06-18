class Solution:
    def leaders(self, arr):
        n=len(arr)
        leaders=[]
        right_leaders=arr[n-1]
        leaders.append(right_leaders)
        for i in range (n-2,-1,-1):
            if arr[i]>=right_leaders:
                right_leaders=arr[i]
                leaders.append(arr[i])
        return leaders[::-1]
        