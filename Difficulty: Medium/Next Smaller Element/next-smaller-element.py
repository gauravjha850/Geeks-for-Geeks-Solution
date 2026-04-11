class Solution:
	def nextSmallerEle(self, arr):
		n=len(arr)
		result=[-1]*n
		stack=[]
		for i in range (n-1,-1,-1):
		    while stack and stack[-1]>=arr[i]:
		        stack.pop()
		    if not stack :
		        result[i]= -1
	        else:
	            
	            result[i]= stack[-1]
		    stack.append(arr[i])
	    return result