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

	def role_assign(self, user_id, role_id):
		driver = self.driver
		elem = driver.find_element_by_id("username")
		user = config('NOTIFICATION_USER').split(',')
		elem.send_keys(user[user_id])
		role = config('NOTIFICATION_ROLE').split(',')
		elem = driver.find_element_by_id("role")
		elem.send_keys(role[role_id])
		driver.findElement(By.xpath("//button[@value='add']")).click()


	def test_assigning_roles(self):
		driver = self.driver
		self.login(3)
		self.role_assign(1,1)		# making the publisher
		self.role_assign(0,0)		# joining the tester_notifications in this community
		self.role_assign(2,0)		# joining the user_notifications in this community
		

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()

