#User function Template for python3

class Solution:
    def removeOuter(self, S):
        result=[]
        stack_len=0
        for ch in S :
            if ch =='(':
                if stack_len>0:
                    result.append(ch)
                stack_len += 1
            else:
                stack_len=stack_len -1
                
                if stack_len >0:
                    result.append(ch)
        return "".join(result)
            