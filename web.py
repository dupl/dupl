#!/usr/bin/python
#coding:utf-8
from selenium import webdriver
import getpass
passwd = getpass.getpass('Password:')
browser = webdriver.Firefox()
#browser.get('http://www.ustc.edu.cn')
#linkElem = browser.find_element_by_link_text(u'电子邮件')
#linkElem.click() # follows the "电子邮件" link
browser.get('http://mail.ustc.edu.cn')
uidElem = browser.find_element_by_id('uid')
uidElem.send_keys('dupl@mail.ustc.edu.cn')
passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys(passwd)
loginElem = browser.find_element_by_id('login_button')
loginElem.click()
