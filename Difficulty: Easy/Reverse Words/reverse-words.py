class Solution:
    def reverseWords(self, s):
        
        words=s.split('.')
        result=[]
        for i in range (len(words)-1,-1,-1):
            
            
            if words[i] !="":
                result.append(words[i])
        return ".".join(result)
        
        