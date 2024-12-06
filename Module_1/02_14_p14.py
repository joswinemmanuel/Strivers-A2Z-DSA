def nLetterTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(chr(64+j), end=" ")
        print()
