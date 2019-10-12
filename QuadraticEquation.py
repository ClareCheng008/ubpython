#!/usr/bin/env python3
import math
a = float(input("Please ax^2 a:"))
b = float(input("Please bx b:"))
c = float(input("Please c:"))
d = b * b - 4 * a * c
if d < 0:
    print("invalid input para.")
else:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print("answer1 is {:4.4}".format(r1))
    print("answer2 is {:4.4}".format(r2))




    

