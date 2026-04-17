#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        if not arr :
            return ""
        
        for i in range (len(arr[0])):
            char=arr[0][i]
            for j in range (1,len(arr)):
                if i == len(arr[j]) or arr[j][i]!=char :
                    return arr[0][:i]
        return arr[0]