def nStarTriangle(n: int) -> None:
    for i in range(n):
        
        for j in range(n-(i+1)):
            print(" ", end="");

        for j in range((i*2)+1):
            print("*", end="")

        for j in range(n-i):
            print(" ", end="")

        print()
