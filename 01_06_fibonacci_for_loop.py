from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    fib1, fib2 = 1, 1
    fib3 = fib1 + fib2
    for i in range(n-3):
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib3
    print(fib3)
