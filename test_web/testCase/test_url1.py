#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import unittest
from base_page import BasePage
import request_geturl as rg

class Test(unittest.TestCase):
	
	def setUp(self):
		self.brower=BasePage()
		'''
		params={"user_token":'market_12'}
		text=rg.request_post("https://fulldev.yjifs.com/tools/tools/get_technical_choose_data?technical_name=KDJ1")
		text_urls=test['datas']
		for url in text_url:
		'''
		self.url='http://ad.cjs.com.cn/template/html/81/5b46bbcbcb081.html'
		self.brower.open_url(self.url)
		
	def test_nbsr(self):
		#股票代码输入
		self.brower.type('//*[@id="gp"]',6)
		self.assertEqual(self.brower.driver.title,u"精准测股系统")
		time.sleep(2)
		self.brower.click("/html/body/div[3]/div[1]/div[2]/div[2]/ul/div/div[1]")
		time.sleep(2)
		self.brower.click('//*[@id="btnSave"]')
		self.brower.type('//*[@id="mobilePhone"]',17623250366)
		#领取
		self.brower.click("/html/body/div[1]/div/div/div/ul/li[3]/button")
		time.sleep(2)
		#已注册弹窗提示
		self.al=self.brower.driver.switch_to.alert
		self.assertEqual(self.al.text,u"已注册手机号！")
		time.sleep(2)
		self.brower.quit_url()
		
if __name__ == "__main__":
	unittest.main()
