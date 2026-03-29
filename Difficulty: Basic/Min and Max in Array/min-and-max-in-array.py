class Solution:
    def getMinMax(self,arr):
        return self.solve(arr,0,len(arr)-1)
    def solve(self,arr,i,j):
        if i==j:
            
            return arr[i],arr[i]
        elif i==j-1:
            if arr[i]<arr[j]:
                return arr[i],arr[j]
            else:
                return arr[j],arr[i]
        
        mid=i+(j-i)//2
        min1,max1=self.solve(arr,i,mid)
        min2,max2=self.solve(arr,mid+1,j)
        return min(min1,min2),max(max1,max2)
        
        