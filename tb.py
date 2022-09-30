import time

from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
import options
from selenium.webdriver.common.by import By
import time
import datetime

if __name__ == '__main__':
    # 导入浏览器
    driver = options.edge_option()
    # 全屏页面
    driver.maximize_window()
    # 打开京东
    driver.get("https://cart.taobao.com/cart.htm?spm=a1z02.1.a2109.d1000367.PXJ3MN&nekot=1470211439694")

    d = input(type)
    d = int(d)

    b = time.time()
    a = d - b
    time.sleep(a)

    # driver.execute_script()
    # 请求浏览器信息
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[4]/div[2]/div[3]/div[5]/a").click()
    # driver.find_element(By.ID,"J_Go")
    driver.implicitly_wait(5)
    # driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/div[1]/div/div[9]/div/div/a[2]").click()
    driver.find_element(By.CLASS_NAME, "go-btn").click()

    input("按 回车 退出程序")
