class Solution:
    def celebrity(self, mat):
        low=0
        n=len(mat)
        high=n-1
        while low  < high :
            if mat[low][high]==1:
                low=low+1
            
                
            else:
                high=high-1
                
        
        candidate = low
        for i in range (n):
            if i !=candidate :
                
        
                if mat[candidate][i]==1 or mat[i][candidate]==0:
                    return -1
        return candidate