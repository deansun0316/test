#! /usr/bin/env python
import rospy
rospy.init_node("lesson2")

num = []
i=0
a=0
for i in range(1,11,2):
    num += [i]
print(num)  
print(max(num))
print(min(num))
print(sum(num))
   
