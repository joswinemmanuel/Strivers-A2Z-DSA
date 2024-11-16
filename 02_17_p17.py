def alphaHill(n: int):
    # Write your solution from here.
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end=" ")
        digit = 64
        for j in range((i-1)*2+1):
            if(j < i):              
                digit += 1
            else:
                digit -= 1
            print(chr(digit), end=" ")      
        print()
        
