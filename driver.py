from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
import options

if __name__ == '__main__':
    driver = options.edge_option()
    driver.get("https://baidu.com")

    # input("按 回车 退出程序")
