#!/usr/bin/env python

import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class NavBarActions(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(command_executor='http://'+config('DOCKER_IP')+':'+config('DOCKER_PORT')+'/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)

	def test_navbar_wiki(self):
		driver = self.driver
		# Logging in by admin
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('CONTENT_TOOLS_PORT')+"/login")
		elem = driver.find_element_by_id("id_username")
		user = config('CONTENT_TOOLS_USER').split(",")
		elem.send_keys(user[3])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('CONTENT_TOOLS_PASSWORD'))
		driver.find_element_by_class_name('btn-block').click()
		driver.find_element_by_xpath('//a[@href="/communities/"]').click()
		driver.find_element_by_xpath('//a [@href="/community-view/' + config('CONTENT_TOOLS_COMMUNITY_ID') + '/"]').click()
		community_name = driver.find_element_by_xpath('//li [@class="breadcrumb-item active"]').text
		driver.find_element_by_xpath('//a[@href="/wiki/' + community_name + config('CONTENT_TOOLS_COMMUNITY_ID') + '"]').click()
		print (driver.current_url)


	def tearDown(self):
        	self.driver.quit()

if __name__ == '__main__':
	unittest.main()
