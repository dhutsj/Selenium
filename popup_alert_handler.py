# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox(executable_path=r'C:\Users\geckodriver.exe')  # Get local session of firefox
browser.get("https://www.baidu.com/")
shezhi = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[8]')
browser.implicitly_wait(5)
webdriver.ActionChains(browser).move_to_element(shezhi).perform()
sousuo = browser.find_element_by_css_selector('.setpref')
browser.implicitly_wait(5)
sousuo.click()
baocunshezhi = browser.find_element_by_css_selector('.prefpanelgo')
time.sleep(5)
baocunshezhi.click()
browser.switch_to_alert().accept()
browser.quit()
