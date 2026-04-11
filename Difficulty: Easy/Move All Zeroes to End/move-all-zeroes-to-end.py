class Solution:
	def pushZerosToEnd(self, arr):
    	low=0
    	high=len(arr)
    	for i in range (high):
    	    if arr[i]!=0:
    	        arr[low],arr[i]=arr[i],arr[low]
                low=low+1        
        return arr
                
	        