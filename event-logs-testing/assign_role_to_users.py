__author__= 'Minali and Urmi'

# This script should assign the following roles to users:
# tester_contenttools should join the "Test Community"
# publisher_contenttools should be given the role of publisher in the community
# user_contenttools should join the "Test Community"
# newuser_contenttools should not be a member of this community.



import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class create_env(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(command_executor='http://'+config('DOCKER_IP')+':'+config('DOCKER_PORT')+'/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)

	def login(self,var):
		driver = self.driver
		driver.get("http://" + config('IP_ADDRESS')+ ":" + config('PORT'))
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('PORT') + '/login/?next=/')
		elem = driver.find_element_by_id("id_username")
		user = config('EVENT_LOGS_USER').split(',')
		elem.send_keys(user[var])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('EVENT_LOGS_PASSWORD'))
		driver.find_element_by_class_name('btn-block').click()

	def role_assign(self, user_id, role_id):
		driver = self.driver
		elem = driver.find_element_by_id("username")
		user = config('EVENT_LOGS_USERS').split(',')
		elem.send_keys(user[user_id])
		role = config('EVENT_LOGS_ROLE').split(',')
		elem = driver.find_element_by_id("role")
		elem.send_keys(role[role_id])
		#driver.find_element_by_id('add').click()
		driver.find_element_by_xpath("//button [@type='submit' and @value='add']").click()


	def test_assigning_roles(self):
		driver = self.driver
		self.login(3)
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('PORT') + '/communities/')
		driver.find_element_by_xpath('//a [@href="/community-view/' + config('EVENT_LOGS_COMMUNITY_ID') + '/"]').click()
		print (driver.current_url)
		driver.find_element_by_xpath('//a [@href="/manage_community/' + config('EVENT_LOGS_COMMUNITY_ID') + '/"]').click()
		self.role_assign(1,1)		# making the publisher
		self.role_assign(0,0)		# joining the tester_notifications in this community
		self.role_assign(2,0)		# joining the user_notifications in this community
		

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()

