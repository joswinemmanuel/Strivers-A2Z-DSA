class Solution:    
    #Complete this function
    def printNos(self,n):
        #Your code here
        if n>0 :
            self.printNos(n-1)
            print(n, end=" ")
