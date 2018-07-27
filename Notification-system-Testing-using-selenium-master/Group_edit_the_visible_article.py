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
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT'))
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/login/?next=/')
		elem = driver.find_element_by_id("id_username")
		user = config('NOTIFICATION_USER').split(',')
		elem.send_keys(user[var])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('NOTIFICATION_PASSWORD'))
		driver.find_element_by_class_name('btn-block').click()

	def test_editVisibleArticle(self):	
		driver = self.driver
		# only community admin and community publisher can edit an article which is in visible state
		for i in range(1,2):
			self.login(i)
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/communities/')
			driver.find_element_by_xpath('//a [@href="/community-view/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
			driver.find_element_by_xpath('//a [@href="/group-view/' + config('NOTIFICATION_GROUP_ID') + '/"]').click()
			driver.find_element_by_xpath('//a [@href="/group_content/' + config('NOTIFICATION_GROUP_ID') + '/"]').click()
			driver.find_element_by_xpath('//a [@href="/article-view/' + config('NOTIFICATION_GROUP_ARTICLE_ID') + '/"]').click()
			driver.find_element_by_xpath('//a [@href="/article-edit/' + config('NOTIFICATION_GROUP_ARTICLE_ID') + '/"]').click()
			driver.find_element_by_id('savechanges').click()
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT'))
			self.login(0) # logging in with tester, creater of article
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/notifications/')
			time.sleep(3)
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')


	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()
