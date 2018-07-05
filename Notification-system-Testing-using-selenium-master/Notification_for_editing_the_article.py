__author__= 'shubh'
import unittest
from decouple import config
from selenium import webdriver

class signup(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()

	def login(self,var,driver):
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
		driver = webdriver.Firefox()
		for i in range(0,3):
			self.login(i,driver)
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/communities/')
			driver.find_element_by_xpath('//a [@href="/community-view/2/"]').click()
			driver.find_element_by_xpath('//a [@href="/community_content/2/"]').click()
			#make the id as visible of the button of visible in html file
			driver.find_element_by_xpath('//a [@href="/article-view/7/"]').click()
			driver.find_element_by_xpath('//a [@href="/article-edit/7/"]').click()
			driver.find_element_by_id('savechanges').click()
			driver.implicitly_wait(1000)
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')
			driver.implicitly_wait(100)
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT'))
			self.login(3,driver)
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/notifications/')
			driver.implicitly_wait(100)
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/logout/')
			driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT'))


	@classmethod
	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()