class Solution:
    def sumOfSeries(self,n):
        #code here
        if n == 0:
            return 0
        return n**3 + self.sumOfSeries(n-1)
