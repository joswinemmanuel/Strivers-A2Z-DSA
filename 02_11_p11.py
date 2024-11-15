def nBinaryTriangle(n: int) -> None:
    # Write your solution here.
    digit = 1
    for i in range(1, n+1):
        if i%2==0:
            digit = 0
        else:
            digit = 1
        for j in range(1, i+1):
            print(digit, end=" ")
            digit = 1 - digit
        print()
