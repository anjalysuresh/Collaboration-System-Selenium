__author__= 'shubh'
import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class signup(unittest.TestCase):
	@classmethod
	def setUp(self):
		self.driver = webdriver.Remote(command_executor='http://'+'10.129.132.104'+':4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)

	def login(self,var,driver):
		driver = self.driver
		driver = webdriver.Remote(command_executor='http://'+'10.129.132.104'+':4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)
		driver.get("http://" + config('IP_ADDRESS')+ ":" + config('NOTIFICATION_PORT'))
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/login/?next=/')
		elem = driver.find_element_by_id("id_username")
		user = config('NOTIFICATION_USER').split(',')
		elem.send_keys(user[var])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('NOTIFICATION_PASSWORD'))
		driver.find_element_by_class_name('btn-block').click()

	def test_draftToVisisbleState(self):
		driver = webdriver.Firefox()
		self.login(0,driver)
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/mydashboard/')
		driver.find_element_by_xpath('//a [@href="/article-view/' + config('NOTIFICATION_ARTICLE_ID') + '/"]').click()
		driver.find_element_by_xpath('//a [@href="/article-edit/' + config('NOTIFICATION_ARTICLE_ID') + '/"]').click()
		#make the id as visible of the button of visible in html file
		driver.find_element_by_id('publish').click()
		driver.find_element_by_xpath('//a [@href="/community-view/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
		driver.find_element_by_xpath('//a [@href="/community_feed/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()

		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')
		self.login(1)
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + "/notifications/")

	@classmethod
	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()
