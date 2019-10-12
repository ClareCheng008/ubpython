#!/usr/bin/env python3
a=b=1
print("-" * 50)
for a in range(1,10):
    for b in range(1,a+1):
        print("{}*{}={:<2d}".format(a,b,a*b), end='  ')
    print()
print("-" * 50)


