def triangle( n:int) ->None:
    # Write your solution here.
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end=" ")
        print()
