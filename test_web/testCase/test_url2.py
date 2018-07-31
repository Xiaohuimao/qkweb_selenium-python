import time
import unittest
from base_page import BasePage
import re

class Test(unittest.TestCase):
	def setUp(self):
		self.brower=BasePage()
		self.url='http://ad.cjs.com.cn/template/html/42/5b46bbc2afd42.html'
		self.brower.open_url(self.url)

	#def tearDown(self):
        # 关闭浏览器
		#self.brower.quit_browser()
		
	def test_url2(self):
		self.brower.type('//*[@id="mobilePhone"]',17623250366)
		#self.assertEqual(self.brower.driver.title,u"精准测股系统")
		time.sleep(2)
		self.brower.click("/html/body/div[11]/div/a")
		time.sleep(2)
		'''
		time.sleep(2)
		self.brower.click('//*[@id="btnSave"]')
		self.brower.type('//*[@id="mobilePhone"]',17623250366)
		time.sleep(10)
		#self.brower.d()
		#self.brower.get_page_source()
		#领取
		self.brower.click("/html/body/div[1]/div/div/div/ul/li[3]/button")
		time.sleep(10)
		#已注册弹窗提示
		self.al=self.brower.driver.switch_to.alert
		self.assertEqual(self.al.text,u"已注册手机号！")
		time.sleep(2)
		'''
		self.brower.quit_url()
if __name__ == "__main__":
	unittest.main()
