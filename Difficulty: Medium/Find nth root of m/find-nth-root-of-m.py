class Solution:
    def nthRoot(self, n, m):
        if m==0 :
            return 0
        if m==1:
            return 1
        
        
            
        low=1
        high=m
        while low <= high :
            mid =low+(high-low)//2
            val=mid**n
            
            
            if val==m:
                
                
                return mid
            if val< m:
                low=mid+1
            else:
                high=mid-1
        return -1
            
            
    
       
 