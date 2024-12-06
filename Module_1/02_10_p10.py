def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        for j in range(n-(i+1)):
            print(" ", end="")
        print()
    for i in range(n-1, 0, -1):
        for j in range(i):
            print("*", end="")
        for j in range((n-1)-i + 1):
            print(" ", end="")
        print()
