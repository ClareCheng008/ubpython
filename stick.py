#!/usr/bin/env python3
import time
import random
sticks = 21
while True:
    print("Stick left: {}".format(sticks))
    if sticks == 1:
        print("you took the last stick, you loose")
        break
    stick_own = int(input("Take stick(1-4):"))
    if stick_own > 4 or stick_own < 1:
        print("wrong choice")
        continue
    sticks -= stick_own
    #time.sleep(1)
    print("Stick left: {}".format(sticks))
    if sticks == 1:
        print("npc took the last stick, it loose")
        break
    stick_npc = random.randint(1,4)
    print("npc took sticks: {}".format(stick_npc))
    #stick_npc = 5 - stick_own
    sticks -= stick_npc





