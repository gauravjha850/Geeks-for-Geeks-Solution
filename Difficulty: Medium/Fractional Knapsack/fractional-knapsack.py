class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        
        n=len(val)
        items=[]
        for i in range (n):
            ratio=val[i]/wt[i]
            
            items.append((val[i],wt[i],ratio))
            
        items.sort(key=lambda x: x[2],reverse=True)
        
        total_value=0.0
        for v,w,r in items:
            if capacity >= w:
                total_value+=v
                capacity-=w
            else:
                total_value+= v*(capacity/w)
                break
        return total_value
        
        
        