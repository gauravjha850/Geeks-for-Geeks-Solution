class Solution:

	def findLargest(self, arr):
	    sorted_str=[str(i) for i in arr]
	    sorted_arr=self.merge_sort(sorted_str)
	    
	    result="".join(sorted_arr)
	    
	    return "0" if result[0]=="0" else result
	def merge_sort(self,arr):
	    if len(arr)<=1:
	        return arr
	    mid=len(arr)//2
	    
	    left_arr=self.merge_sort(arr[:mid])
	    right_arr=self.merge_sort(arr[mid:])
	    
	    return self.merge(left_arr,right_arr)
	def merge(self,left,right):
	    i=0
	    j=0
	    merged=[]
	    while i<len(left) and j<len(right):
	        if left[i]+right[j]> right[j]+left[i]:
	            merged.append(left[i])
	            i+=1
	        else:
	            merged.append(right[j])
	            j+=1
	    merged.extend(left[i:])
	    merged.extend(right[j:])
	        
	    return merged
	       
	            
	
	    