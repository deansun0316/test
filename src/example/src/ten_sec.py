#! /usr/bin/env python 
from time import sleep
n=1
while n<11:
     if n==10:
         sleep(1)
         print("time out")
         n+=1
     elif n<10:
         sleep(1)
         print(n)
         n+=1

