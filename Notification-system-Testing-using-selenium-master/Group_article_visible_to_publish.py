# creater of an article cannot publish the article

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

	def test_visisbleToPublishState(self):	
		driver = self.driver
		self.login(1) # logging in with publisher since from visible state, article can be published or rejected only by users who have roles like community_publisher/group_admin/community_admin 
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/communities/')
		print (driver.current_url)
		driver.find_element_by_xpath('//a [@href="/community-view/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
		print (driver.current_url)
		time.sleep(3)
		driver.find_element_by_xpath('//a [@href="/group-view/' + config('NOTIFICATION_GROUP_ID') + '/"]').click()
		print (driver.current_url)
		time.sleep(3)
		driver.find_element_by_xpath('//a [@href="/group_content/' + config('NOTIFICATION_GROUP_ID') + '/"]').click()
		print (driver.current_url)
		driver.find_element_by_xpath('//a [@href="/article-view/' + config('NOTIFICATION_GROUP_ARTICLE_ID') + '/"]').click()
		driver.find_element_by_xpath('//a [@href="/article-edit/' + config('NOTIFICATION_GROUP_ARTICLE_ID') + '/"]').click()
		driver.find_element_by_id('state_change_id').click()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/articles/')
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')
		for i in range(1,4):
			self.login(i)
			driver.find_element_by_xpath('//a [@href="/notifications/"]').click()
			driver.get("http://" + config('IP_ADDRESS') + '/logout/')

	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()
