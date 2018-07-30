#!/usr/bin/env python

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os

class TestJoinUSButton(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
		
	def test_join_us(self):
		self.driver.get("http://172.17.0.1:7000/login/")
		user ="root"
	        pwd= "root1234"
	        elem = self.driver.find_element_by_id("id_username")
	        elem.send_keys(user)
	        elem = self.driver.find_element_by_id("id_password")
	        elem.send_keys(pwd)
	        self.driver.find_element_by_class_name('btn-block').click()
		self.driver.find_element_by_xpath('//a[@href="/communities/"]').click()
		self.driver.find_element_by_xpath('//a[@href="/community-view/1/"]').click()
		self.driver.find_element_by_class_name("btn.btn-success").click()
		self.driver.find_element_by_id("content")
		
	def tearDown(self):
		self.driver.quit();
		
if __name__ == '__main__':
	unittest.main()
