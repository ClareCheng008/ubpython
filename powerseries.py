#!/usr/bin/env python3
x = float(input("Please input a x value:"))
i = 1
tmp = 1.0
result = 1.0
while i < 10000000:
    tmp *= x/i
    result += tmp
    i += 1
    if tmp < 0.00001:
        break
print("Times: {} e^{}={:.20}".format(i,x,result))


