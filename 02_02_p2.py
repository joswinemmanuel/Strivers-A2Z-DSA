def nForest(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print("* ", end=" ")
        print()
