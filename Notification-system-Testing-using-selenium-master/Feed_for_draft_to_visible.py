__author__= 'shubh'

import time
import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class signup(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(command_executor='http://'+'10.129.132.104'+':4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)


	def test_draftToVisisbleState(self):
		driver = self.driver
		driver = webdriver.Remote(command_executor='http://'+'10.129.132.104'+':4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT'))
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/login/?next=/')
		elem = driver.find_element_by_id("id_username")
		user = config('NOTIFICATION_USER').split(',')
		elem.send_keys(user[0])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('NOTIFICATION_PASSWORD'))
		driver.find_element_by_class_name('btn-block').click()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/mydashboard/')
		e = driver.find_element_by_id("myArticles_info");
		driver.find_element_by_xpath('//a [@href="/article-view/' + config('NOTIFICATION_ARTICLE_ID') + '/"]').click()
		driver.find_element_by_xpath('//a [@href="/article-edit/' + config('NOTIFICATION_ARTICLE_ID') + '/"]').click()
		print(driver.current_url)
		time.sleep(5)
		driver.find_element_by_id('publish').click()
		time.sleep(5)
		print(driver.current_url)
		driver.find_element_by_xpath('//a [@href="/community-view/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
		driver.find_element_by_xpath('//a [@href="/community_feed/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()
