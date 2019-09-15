#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://www.ustc.edu.cn')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
# scrolls to bottom
htmlElem.send_keys(Keys.HOME)
# scrolls to top
