class Solution:

    def minJumps(self, arr):

        if len(arr) <= 1:
            return 0

        if arr[0] == 0:
            return -1

        maxReach = arr[0]
        step = arr[0]
        jump = 1

        for i in range(1, len(arr)):

            if i == len(arr) - 1:
                return jump

            maxReach = max(maxReach, i + arr[i])

            step -= 1

            if step == 0:

                jump += 1

                if i >= maxReach:
                    return -1

                step = maxReach - i

        return -1
