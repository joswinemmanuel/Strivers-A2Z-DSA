class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        def bubbleRecursive(arr, n):
            if n==1:
                return
            for j in range(n-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            bubbleRecursive(arr, n-1)
        bubbleRecursive(arr, n)
