__author__= 'shubh'
import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class signup(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Remote(command_executor='http://'+config('DOCKER_IP')+':'+config('DOCKER_PORT')+'/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)

	def login(self,var):
		driver = self.driver
		driver.get("http://" + config('IP_ADDRESS')+ ":" + config('NOTIFICATION_PORT'))
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/login/?next=/')
		elem = driver.find_element_by_id("id_username")
		user = config('NOTIFICATION_USER').split(',')
		elem.send_keys(user[var])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('NOTIFICATION_PASSWORD'))
		driver.find_element_by_class_name('btn-block').click()

	def test_visibleRejectedToPrivateState(self):	
		driver = self.driver
		self.login(1) # logging in with publisher who is Community Admin and can hence publish/reject and has not made the article visible himself
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/communities/')
		driver.find_element_by_xpath('//a [@href="/community-view/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
		print (driver.current_url)
		driver.find_element_by_xpath('//a [@href="/group-view/' + config('NOTIFICATION_GROUP_ID') + '/"]').click()
		print (driver.current_url)
		driver.find_element_by_xpath('//a [@href="/group_content/' + config('NOTIFICATION_GROUP_ID') + '/"]').click()
		print (driver.current_url)
		driver.find_element_by_xpath('//a [@href="/article-view/' + config('NOTIFICATION_GROUP_ARTICLE_ID') + '/"]').click()
		print (driver.current_url)
		driver.find_element_by_xpath('//a [@href="/article-edit/' + config('NOTIFICATION_GROUP_ARTICLE_ID') + '/"]').click()
		print (driver.current_url)
		driver.find_element_by_id('reject').click()
		print (driver.current_url)
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/communities/')
		driver.find_element_by_xpath('//a [@href="/community-view/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
		driver.find_element_by_xpath('//a [@href="/group-view/' + config('NOTIFICATION_GROUP_ID') + '/"]').click()
		driver.find_element_by_xpath('//a [@href="/group-feed/' + config('NOTIFICATION_GROUP_ID') + '/"]').click()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')
		for i in range(1,3):
			self.login(i)
			driver.find_element_by_xpath('//a [@href="/notifications/"]').click()
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')


	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()
