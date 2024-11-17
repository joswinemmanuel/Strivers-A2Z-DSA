class Solution:
    def evenlyDivides(self, n):
        # code here
        count = 0
        for i in str(n):
            if i != '0' and n % int(i) == 0:
                count += 1
        return count
