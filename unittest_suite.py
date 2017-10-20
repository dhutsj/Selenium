# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import unittest

class router(unittest.TestCase):
        def setUp(self):
            global browser
            browser = webdriver.Firefox(executable_path=r'C:\Users\geckodriver.exe')  # Get local session of firefox
            browser.get("https://192.168.2.1")  # Load page
            time.sleep(10)
            elem_login = browser.find_element_by_id("user-name")
            elem_login.click()
            elem_login.send_keys("cisco")
            elem_password = browser.find_element_by_id("user-password")
            elem_password.click()
            elem_password.send_keys("cisco")
            elem = browser.find_element_by_id("login-btn")
            elem.click()
            time.sleep(5)
            self.assertTrue('RV160-router540247' in browser.page_source)
        def test_AddVLan(self):
            lan_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/table/tbody/tr[7]/td/table[1]/tbody/tr/td[3]")
            lan_button.click()
            time.sleep(3)
            vlan_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/table/tbody/tr[7]/td/table[2]/tbody/tr[3]/td[3]")
            vlan_button.click()
            time.sleep(3)
            add_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/form/div[3]/div[1]/div/div[1]/a/i")
            add_button.click()
            time.sleep(3)
            input1 = browser.find_element_by_xpath("//*[@id=\"vlan-id3\"]")
            input1.send_keys("120")
            input2 = browser.find_element_by_xpath("//*[@id=\"description3\"]")
            input2.send_keys("vlan for selenium test")
            apply_button = browser.find_element_by_xpath("//*[@id=\"page-apply-btn\"]")
            apply_button.click()
            time.sleep(5)
            self.assertTrue("vlan for selenium test" in browser.page_source)
        def test_deleteVLan(self):
            lan_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/table/tbody/tr[7]/td/table[1]/tbody/tr/td[3]")
            lan_button.click()
            time.sleep(3)
            vlan_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/table/tbody/tr[7]/td/table[2]/tbody/tr[3]/td[3]")
            vlan_button.click()
            time.sleep(3)
            label = browser.find_element_by_xpath("//*[@id=\"icheck3_lb\"]")
            label.click()
            delete_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/form/div[3]/div[1]/div/div[3]/a/i")
            delete_button.click()
            time.sleep(3)
            self.assertFalse("vlan for selenium test" in browser.page_source)
        def tearDown(self):
            browser.quit()


if __name__ == "__main__":
        test_cases = unittest.TestLoader().loadTestsFromTestCase(router)
        # 使用测试套件并打包测试用例
        test_suit = unittest.TestSuite()
        test_suit.addTests(test_cases)
        # 运行测试套件，并返回测试结果
        test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
        # 生成测试报告
        print("testsRun:%s" % test_result.testsRun)
        print("failures:%s" % len(test_result.failures))
        print("errors:%s" % len(test_result.errors))
        print("skipped:%s" % len(test_result.skipped))



