#!/usr/bin/env python3
n = int(input("Please input the student number:"))
subject = ('Chinese', 'Math', 'English')
data={}
for i in range(1,n+1):
    name = input("student[{}]'s name: ".format(i))
    for s in subject:
        score = int(input("{}: ".format(s)))
        data.setdefault(name,[]).append(score)
print(data)
for x, y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "Fail:(")
    else:
        print(x, "Pass:)")
    

