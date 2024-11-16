def alphaTriangle(n: int):
    # Write your solution here.
    for i in range(n, 0, -1):
        for j in range(n, i-1, -1):
            print(chr(64+j), end=" ")
        print()
