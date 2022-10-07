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
    driver.get(
        "https://laputa.alibaba-inc.com/?spm=a26311.21140922.0.dhighseas.4f314a2csTtpnV&_path_=crm/indexChannel/high_seas")

    d = input(type)
    z = input(type)
    d = int(d)
    z = str
    b = time.time()
    a = d - b
    time.sleep(a)

    # driver.execute_script()
    # 请求浏览器信息
    # <button type="button" class="next-btn next-btn-primary next-btn-medium" style="margin-right: 10px;"><!-- react-text: 14 -->确定<!-- /react-text --></button>
    # /html/body/div[7]/div/div/div/div[2]/div/div/div/div[1]/button[1]
    driver.find_element(By.XPATH, z).click()
    # driver.find_element(By.LINK_TEXT, "确定").click()
    # driver.find_element(By.CLASS_NAME, "next-btn.next-btn-primary.next-btn-medium").click()
    # driver.find_element(By.ID,"J_Go")

    input("按 回车 退出程序")
