def isArmstrong(n):
    number = str(n)
    count = len(number)
    sum = 0
    for i in number:
        sum += int(i)**count
    if sum == n:
        return True
    else:
        return False
