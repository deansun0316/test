#! /usr/bin/env python
import rospy
x =[]
for i in range(3):
    a = input()
    x.append(a)
x=sorted(x)
print(x)

