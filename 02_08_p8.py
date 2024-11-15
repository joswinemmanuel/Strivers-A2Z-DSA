def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(" ", end="")
        for j in range((i-1)*2 + 1):
            print("*", end="")
        for j in range(n-i):
            print(" ", end=" ")
        print(a)
