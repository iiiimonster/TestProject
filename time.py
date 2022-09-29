#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : zwy
# @time    : 2022/9/20 10:10
# @function: the script is used to do something.
# @version : 
#   V1 
#
import time

t = time.time_ns()
print(t)
t = time.time()
print(t)

# 需要到达得时间 减去当前时间 获取等待时间
a = 1664420700 - t
print(a)

time.sleep(a)
print(time.time())
