class Solution:
    def printGfg(self, n):
        # Code here
        if n == 0:
            return
        print("GFG", end=" ")
        self.printGfg(n-1)
