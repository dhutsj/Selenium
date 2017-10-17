# -*- coding: UTF-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path=r'C:\Users\geckodriver.exe')
driver.get("http://www.baidu.com")
time.sleep(2)

#id = cp 元素的文本信息
data=driver.find_element_by_id("cp").text
print data   #打印信息

time.sleep(3)
driver.quit()

'''
id_

#当前元素的ID



tag_name

#获取元素标签名的属性



text

#获取该元素的文本。



click()

#单击（点击）元素



submit()

#提交表单



clear()

#清除一个文本输入元素的文本



get_attribute(name)

#获得属性值



s_selected(self)

#元素是否被选择

Whether the element is selected.

is_enabled()

#元素是否被启用



find_element_by_id(id_)

find_elements_by_id(id_)

#查找元素的id 



find_element_by_name(name)

find_elements_by_name(name)

#查找元素的name



find_element_by_link_text(link_text)

find_elements_by_link_text(link_text)

#查找元素的链接文本



find_element_by_partial_link_text(link_text)

find_elements_by_partial_link_text(link_text)

#查找元素的链接的部分文本



find_element_by_tag_name(name)

find_elements_by_tag_name(name)

#查找元素的标签名



find_element_by_xpath(xpath)

#查找元素的xpath



find_elements_by_xpath(xpath)

#查找元素内的子元素的xpath



find_element_by_class_name(name)

#查找一个元素的类名



find_elements_by_class_name(name)

#查找元素的类名



find_element_by_css_selector(css_selector)

#查找并返回一个元素的CSS 选择器



find_elements_by_css_selector(css_selector)

#查找并返回多个元素的CSS 选择器列表



send_keys(*value)

#模拟输入元素
'''