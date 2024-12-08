class Solution:
    def insertionSort(self, arr):
        #code here
        n = len(arr)
        
        def insertionRecursive(arr, i, n):
            if i==n:
                return
            
            j = i
            while j>0 and arr[j-1]>arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j = j-1
           
            insertionRecursive(arr, i+1, n)
        
        insertionRecursive(arr, 0, n)
