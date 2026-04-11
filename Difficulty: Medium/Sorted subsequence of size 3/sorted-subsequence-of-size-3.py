class Solution:
    def find3Numbers(self, arr):
        n=len(arr)
        
        min_value=[0]*n
        min_index=0
        for i in range(n):
            if arr[i] < arr[min_index]:
                min_index=i
            min_value[i]=min_index
        max_value=[0]*n
        max_index=n-1
        max_value[n-1]=n-1
        for i in range(n-2,-1,-1):
            if arr[max_index]<arr[i]:
                max_index=i
            max_value[i]=max_index
        for j in range (n):
            left_min=arr[min_value[j]]
            current=arr[j]
            right_large=arr[max_value[j]]
            
            if left_min < current < right_large :
                return [left_min,current,right_large]
        return []
        
                
            