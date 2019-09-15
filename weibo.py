#!/usr/bin/python
#coding:utf-8
from selenium import webdriver
import getpass
import time
import random
passwd = getpass.getpass('Password:')
browser = webdriver.Firefox()
browser.get('https://weibo.com')
time.sleep(4)
#print browser.current_url
uidElem = browser.find_element_by_id('loginname')
uidElem.send_keys('18856034388')
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(passwd)
#passwordElem.submit()
loginElem = browser.find_elements_by_link_text(u'登录')
#print loginElem
loginElem[1].click()
#print browser.current_url
time.sleep(6)
while True:
    try:
        textElem = browser.find_element_by_tag_name('textarea')
        linkElem = browser.find_element_by_link_text(u'发布')
        time.sleep(2)
        textElem.send_keys(random.randint(0,100)*u'[并不简单]')
        linkElem.click()
    except:
        pass
