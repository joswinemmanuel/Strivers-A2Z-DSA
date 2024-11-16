def symmetry(n: int):
    # Write your solution from here.
    for i in range(1, n+1):
        for j in range(n, i-1, -1):
            print("* ", end="")
        for j in range((i-1)*2):
            print(" ", end=" ")
        for j in range(n, i-1, -1):
            print("* ", end="")
        print()

    for i in range(1, n+1):
        for j in range(1, i+1):
            print("* ", end="")
        for j in range((n-i)*2):
            print(" ", end=" ")
        for j in range(1, i+1):
            print("* ", end="")
        print()
