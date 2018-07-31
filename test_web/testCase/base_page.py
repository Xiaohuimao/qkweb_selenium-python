#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os.path
#from framework.logger import Logger
 
#创建一个logger实例
#logger = Logger(logger="BasePage").getlog()
 
 
class BasePage(object):
	
	#定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
	
	def __init__(self):
		self.driver = webdriver.Firefox()
		
	def setUp(self,url):
		self.brower=BasePage()
		self.url=url
		self.brower.open_url(self.url)
		
	#打开url
	def open_url(self,url):
		self.driver.get(url)
	#关闭浏览器
	def quit_url(self):
		self.driver.quit()
		
    # 浏览器前进操作
	def forward(self):
		self.driver.forward()
 
    # 浏览器后退操作
	def back(self):
		self.driver.back()
 
    # 隐式等待
	def wait(self, seconds):
		self.driver.implicitly_wait(seconds)
 
    # 点击关闭当前窗口
	def close(self):
		self.driver.close()
 
    # 保存图片
	def get_windows_img(self):
		#在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
		file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
		rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
		screen_name = file_path + rq + '.png'
		try:
			self.driver.get_screenshot_as_file(screen_name)
		except NameError as e:
			self.get_windows_img()
 
    #定位元素方法

    #输入
	def type(self, selector, text):
		el = self.driver.find_element_by_xpath(selector)
		el.clear()
		try:
			el.send_keys(text)
		except NameError as e:
			self.get_windows_img()
 
    # 清除文本框
	def clear(self, selector):
		el = self.driver.find_element_by_xpath(selector)
		try:
			el.clear()
		except NameError as e:
			self.get_windows_img()
 
    # 点击元素
	def click(self, selector):
		el = self.driver.find_element_by_xpath(selector)
		el.click()
    # 或者网页标题
	def get_page_title(self):
		return self.driver.title
	#获取页面源码
	def get_page_source(self):
		self.jsym=self.driver.page_source
		return self.jsym
    #等待
	def d(self):
		self.driver.switch_to.alert.accept()
	#获取当前页面URL
	def get_url(self):
		self.gurl=self.driver.current_url
		return self.gurl
	@staticmethod
	def setUpClass(self):
		pass
	def tearDownClass(self):
		pass
