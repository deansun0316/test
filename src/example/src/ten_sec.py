#! /usr/bin/env python
import rospy
from time import sleep

t = 1
while t <= 10:
    if t == 10:
        sleep(1)
        print("時間到")
    else :
        sleep(1)
        print(t)
    t += 1
