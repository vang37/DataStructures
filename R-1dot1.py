import sys
import random

a = int(sys.argv[1])
b = int(sys.argv[2])

def multiple(n, m):
    if m == 0:
        return False
    i = n/m
    if i == int(i):
        return True
    else:
        return False

   # if m == 0:
   #     return False
   # return n % m == 0

print(multiple(a, b))
print(multiple(10, 2))
print(multiple(5, 3))
print(multiple(1, -1))
print(multiple(1, 0))
