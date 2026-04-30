import math
from typing import List


class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        numbers=[i for i in range (1,n+1)]
        k=k-1
        
        result=[]
        
        for i in range (n-1,-1,-1):
            fact=math.factorial(i)
            
            index=k//fact
            
            chosen_index=numbers[index]
            
            result.append(str(chosen_index))
            
            numbers.pop(index)
            
            k=k%fact
        return "".join(result)
        
        
