class Solution:
    def findMaxProduct(self, arr):
        n = len(arr)
        if n == 1:
            return arr[0]
            
        neg_count = 0
        modulo = 10**9 + 7
        zero_count = 0
        product = 1
        max_neg = float('-inf')
        has_positive = False

        for num in arr:
            if num == 0:
                zero_count += 1
            elif num < 0:
                neg_count += 1
                max_neg = max(max_neg, num)
                product = (product * abs(num)) % modulo
            else:
                has_positive = True
                product = (product * num) % modulo

        if zero_count == n:
            return 0
            
        if neg_count == 1 and zero_count > 0 and not has_positive:
            return 0

        if neg_count % 2 != 0:
            product = (product * pow(abs(max_neg), modulo - 2, modulo)) % modulo

        return product
            
        
            
        
        