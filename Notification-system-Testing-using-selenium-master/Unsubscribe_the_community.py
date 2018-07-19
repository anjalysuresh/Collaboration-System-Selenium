__author__= 'shubh'
import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class signup(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Remote(command_executor='http://'+'10.129.132.104'+':4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)cls.driver = webdriver.Firefox()

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

	def test_draftToVisisbleState(self):	
		driver = self.driver
		self.login(4)
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/communities/')
		driver.find_element_by_xpath('//a [@href="/community-view/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
		driver.find_element_by_id("Unsubscribe").click()
		driver.find_element_by_id("communityUnsubscribe").click()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/notifications/')
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/communities/')
		driver.find_element_by_xpath('//a [@href="/community-view/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
		driver.find_element_by_xpath('//a [@href="/community_feed/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
		#make the id as visible of the button of visible in html file
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')
			
	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()
