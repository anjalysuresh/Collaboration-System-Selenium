__author__= 'shubh'
import unittest
from decouple import config
from selenium import webdriver

class signup(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()

	def login(self,var,driver):
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
		driver.find_element_by_xpath('//a [@href="/article-view/5/"]').click()
		driver.find_element_by_xpath('//a [@href="/article-edit/5/"]').click()
		#make the id as visible of the button of visible in html file
		driver.find_element_by_id('publish').click()
		driver.find_element_by_xpath('//a [@href="/community-view/2/"]').click()
		driver.find_element_by_xpath('//a [@href="/community_feed/2/"]').click()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')
		self.login(1)
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + "/notifications/")

	@classmethod
	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()