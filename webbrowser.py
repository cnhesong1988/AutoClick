#coding = utf-8
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作
import time

driver = webdriver.Firefox()
driver.set_page_load_timeout(10)
driver.get('http://m.cssn.cn/gxx/')
print 'GET OVER'
driver.find_element_by_xpath("//section/ul/li[1]/a").click()
time.sleep(1)
driver.back()
driver.find_element_by_xpath("//section/ul/li[5]/a").click()
#driver.find_elements_by_class_name("play_add").click()
time.sleep(2)
driver.close()