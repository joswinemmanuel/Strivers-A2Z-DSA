def seeding(n: int) -> None:
    # Write your solution here.
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print("*", end=" ")
        print()
