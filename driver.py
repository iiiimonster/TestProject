import time

from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
import options
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # 导入浏览器
    zhanghao = input("请输入京东账号回车确定：")
    driver = options.edge_option()
    # 全屏页面
    driver.maximize_window()
    # 打开京东
    driver.get("https://www.jd.com/")

    # 请求浏览器信息
    driver.find_element(By.CLASS_NAME, "link-login").click()
    driver.find_element(By.CLASS_NAME, "login-tab.login-tab-r").click()
    time.sleep(2)
    a = driver.find_element(By.ID, "loginname")

    # driver.execute_script()
    time.sleep(2)
    a.send_keys(zhanghao)
    input("按 回车 退出程序")
