class Solution:
    def celebrity(self, mat):
        n=len(mat)
        
        a=0
        b=n-1
        
        while a< b:
            if mat[a][b]==1:
                a=a+1
            else:
                b=b-1
        candidate=a
        for i in range(n):
            if i!=candidate :
                if mat[candidate][i]==1 or mat[i][candidate]==0:
                    
                    return -1
        return  candidate 
        
        