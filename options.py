#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : zwy
# @time    : 2022/9/2 15:44
# @function: the script is used to do something.
# @version :
#   V1

# selenium 4
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#

def edge_option():
    options = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    return options


def chrome_option():
    options = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return options
