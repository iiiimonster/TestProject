#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : zwy
# @time    : 2022/9/5 14:10
# @function: the script is used to do something.
# @version : 
#   V1 
#
import time

from selenium import webdriver  # 导入模块
from selenium.webdriver.common.by import By  # 导入By函数
from selenium import webdriver
from selenium.webdriver.common.by import By

import options

driver = options.edge_option()  # 导入浏览器
driver.maximize_window() #全屏页面
driver.get("https://test.login.heypad.cn/#/login")  # 导入浏览器网址
# 账号
# driver.find_element(By.CLASS_NAME,"el-input__inner").click()#点击账号文本框
time.sleep(2)
driver.find_element(By.CLASS_NAME, "el-input__inner").send_keys("hpzw")  # 输入账号
# 密码
# driver.find_element(By.XPATH,"//input[@class='el-input__inner'][@type='password']").click()#点击密码
time.sleep(2)
driver.find_element(By.XPATH, "//input[@class='el-input__inner'][@type='password']").send_keys("hpzw000")  # 输入密码
# 登录按钮
time.sleep(2)
driver.find_element(By.TAG_NAME, "button").click()  # 点击登录

# 退出登录
time.sleep(3)  # 延迟2M
driver.find_element(By.CLASS_NAME, "signout-wz").click()  # 点击退出登录
# 确定退出
time.sleep(3)  # 延迟2M
driver.find_element(By.CLASS_NAME, "button-submit").click()  # 点击确定退出
time.sleep(3)
driver.quit()  # 关闭网页