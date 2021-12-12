#! /usr/bin/env python
import rospy 
rospy.init_node("practice_python_node")


km_cm=7*1000*100
time_spent=(km_cm//0.123)*60
print(int(time_spent))
