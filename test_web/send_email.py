#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import os,time
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.header import Header


def sendEmail(content,title,from_addr,to_addr,smtp_server,
	,password):
		msg=MIMEText(content,"html",'utf-8')
		msg['To'] = ','.join(to_address)
		msg['From'] = from_name
		server=smtplib.SMTP(smtp_server,25)
		server.login(from_addr,password)
		server.sendmail(from_addr,[to_addr],msg.as_string())
def main():
	TO=['2410655706@qq.com']
	config={
		"from":"1715863457@qq.com",
		"to":To,
		"smtp_server":"smtp.qq.com",
		"password":"gkusqxrexefmeiij"
			}
	title="资源页自动化测试报告"
	file_path="C:/Users/Administrator/qkweb_selenium-python/test_web/testReport/result.html"
	f=open(file_path,"rb")
	mail_body=f.read()
	f.close
	
		
