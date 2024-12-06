class Solution:
    def factorialNumbers(self, n):
    	fact = 1
    	x = 2
    	result = []
    	while fact <= n:
    	    result.append(fact)
    	    fact *= x
    	    x += 1
        return result
