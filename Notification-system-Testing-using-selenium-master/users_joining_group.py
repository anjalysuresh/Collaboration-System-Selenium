__author__= 'Minali and Urmi'

# Before running this script a community named "Test Community" should be created manually and the id of this community must be found out manually.
# This script should assign the following roles to users:
# tester_notifications should join the "Test Community"
# publisher_notifications should be given the role of publisher in the community
# user_notifications should join the "Test Community"
# newuser_notifications should not be a member of this community.
# tester_notifications should create an article in the draft state.


import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class create_env(unittest.TestCase):

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
		print (user[var] + " joined.")


	def test_users_joining_group(self):
		driver = self.driver
		for i in (1,3):
			self.login(i)
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/communities/')
			driver.find_element_by_xpath('//a [@href="/community-view/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
			print (driver.current_url)
			driver.find_element_by_xpath('//a [@href="/group-view/' + config('NOTIFICATION_GROUP_ID') + '/"]').click()
			driver.find_element_by_id('join_us').click()
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')
		

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()


