#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : zwy
# @time    : 2022/9/17 13:48
# @function: the script is used to do something.
# @version : 
#   V1 
#

import options
from selenium.webdriver.common.by import By
if __name__ == '__main__':
    # 导入浏览器
    zhanghao = input("请输入账号：")
    driver = options.edge_option()
    # 全屏页面
    driver.maximize_window()
    # 打开京东
    driver.get("https://system.heypad.cn/")
    mima = input("请输入密码：")

    # 点击账号登录
    driver.find_element(By.CLASS_NAME,"el-input__inner").send_keys(zhanghao)
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[3]/form/div[2]/div/div/input").send_keys(mima)
