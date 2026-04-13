class Solution:
    def kokoEat(self, arr, k):
        low=1
        high=max(arr)
        while low <= high:
            mid =low+(high-low)//2
            total_hours=0
            for pile in arr:
                total_hours+=(pile + mid-1)//mid
                
            if total_hours <= k:
                high=mid-1
            else:
                low=mid+1
        return low 
                
                
        