#!/usr/bin/env python3
row = int(input("Enter the number of rows:"))
n = 1
while n <= row:
    print("*"*n)
    n += 1

print()

n = row
while n > 0:
    print("*"*n)
    n -= 1

n = 1
while n <= row:
    print(" "*(row-n), end=' ')
    print("*"*n)
    n += 1

n = row
while n > 0:
    print(" "*(row-n), end=' ')
    print("*"*n)
    n -= 1
