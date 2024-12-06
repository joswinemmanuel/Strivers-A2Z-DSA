class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        n = len(arr)
        frequency = {}
        
        for i in range(1, n+1):
            frequency[i] = 0
            
        for i in arr:
            frequency[i] += 1
        
        return frequency.values()
