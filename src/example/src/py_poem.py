#! /usr/bin/env python
import rospy 
rospy.init_node("practice_python_node")


x=['床前明月光','疑似地上霜','舉頭望明月','低頭思故鄉']
y=input("找:")
if y=="靜夜思":
    for x in x:
        print(x)
