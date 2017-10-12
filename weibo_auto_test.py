# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import unittest

class weibo(unittest.TestCase):
    def test_login(self):
            browser = webdriver.Firefox(executable_path=r'C:\Users\geckodriver.exe')  # Get local session of firefox
            browser.get("https://weibo.com/login.php")  # Load page
            time.sleep(10)
            elem_login = browser.find_element_by_id("loginname")
            elem_login.click()
            elem_login.send_keys("jszxtsj@163.com")
            elem_password = browser.find_element_by_name("password")
            elem_password.click()
            elem_password.send_keys("DHUtsj1234")
            elem = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[6]/a/span")
            elem.click()
            time.sleep(1.5)
            elem.click()
            time.sleep(15)
            input_box = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[2]/textarea")
            input_box.click()
            input_box.send_keys("I love you, xiong fenfang.")
            send_button = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a")
            send_button.click()
            time.sleep(1)
            send_button.click()
            time.sleep(5)
            shouye = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/div[1]/h3/a')
            shouye.click()
            #browser.page_source.__contains__('I love you')
            time.sleep(3)
            self.assertTrue('I love you' in browser.page_source)

if __name__ == "__main__":
    unittest.main()



