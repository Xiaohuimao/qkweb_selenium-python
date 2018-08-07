#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
#接口获取方法封装
def request_get(url):
	response = requests.get(url)
	return response.json()
	
def request_post(url,params="",headers=""):
	response = requests.post(url,params,headers)
	return response.json()
