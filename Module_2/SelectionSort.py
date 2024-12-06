class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr
