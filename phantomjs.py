#coding = utf-8
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

desiredCap = {'platform': 'ANY', 'browserName': 'phantomjs', 'version': '', 'javascriptEnabled': True}
browser = webdriver.PhantomJS(port=0, desired_capabilities=desiredCap)
browser.get('http://y.qq.com/index.html')
try:
    element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "keyword"))
    )
finally:
    browser.close()
    exit()
print browser.title
print browser.get_cookies()
cookies = browser.get_cookies()
browser.add_cookie(cookies[0])
keyword=browser.find_element_by_id('keyword')
keyword.clear()
keyword.send_keys("you are my hero")
search_form = browser.find_element_by_id('search_form')
print "start"
search_form.click()
time.sleep(10)
print "END"
print browser.title
print browser.current_url
browser.switch_to_frame("contentFrame")
qqmusic_category = browser.find_element_by_xpath("//ol[@id='divsonglist']//li[@class='qqmusic_category']")
script_btn = browser.find_element_by_xpath("//ol[@id='divsonglist']//a[@class='btn_play']")
print "start"
print script_btn

actions = ActionChains(browser)
actions.move_to_element(qqmusic_category)
actions.click(script_btn)
actions.perform()

time.sleep(10)
print "END"
print browser.current_url
browser.close()
