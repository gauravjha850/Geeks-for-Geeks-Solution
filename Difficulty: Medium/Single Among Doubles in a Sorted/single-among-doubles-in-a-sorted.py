class Solution:
    def single(self, arr):
        low=0
        high=len(arr)-1
        while low<high:
            mid=low+(high-low)//2
            if mid%2==1:
                mid=mid-1
            if arr[mid]==arr[mid+1]:
                low=mid+2
            else:
                high=mid
        return arr[low]
        
        