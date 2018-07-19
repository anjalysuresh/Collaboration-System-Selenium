__author__= 'shubh'
import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class signup(unittest.TestCase):
	
	def setUp(self):
	self.driver = webdriver.Remote(command_executor='http://'+'10.129.132.104'+':4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)
	
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

	def test_draftToVisisbleState(self):	
		driver = self.driver
		for i in range(0,3):
			self.login(i)
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/communities/')
			driver.find_element_by_xpath('//a [@href="/community-view/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
			driver.find_element_by_xpath('//a [@href="/community_content/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
			#make the id as visible of the button of visible in html file
			driver.find_element_by_xpath('//a [@href="/article-view/' + config('NOTIFICATION_ARTICLE_ID') + '/"]').click()
			driver.find_element_by_xpath('//a [@href="/article-edit/' + config('NOTIFICATION_ARTICLE_ID') + '/"]').click()
			driver.find_element_by_id('savechanges').click()
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT'))
			self.login(3)
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/notifications/')
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT'))


	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()
