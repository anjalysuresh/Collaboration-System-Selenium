__author__= 'shubh'
import unittest
from decouple import config
from selenium import webdriver

class signup(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_draftToVisisbleState(self):
		driver = webdriver.Firefox()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT'))
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/login/?next=/')
		elem = driver.find_element_by_id("id_username")
		user = config('NOTIFICATION_USER').split(',')
		elem.send_keys(user[0])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('NOTIFICATION_PASSWORD'))
		driver.find_element_by_class_name('btn-block').click()
		driver.get("http://" + config('IP_ADDRESS') + '/mydashboard/')
		driver.find_element_by_xpath('//a [@href="/article-view/4/"]').click()
		driver.find_element_by_xpath('//a [@href="/article-edit/4/"]').click()
		#make the id as visible of the button of visible in html file
		driver.find_element_by_id('publish').click()
		driver.find_element_by_xpath('//a [@href="/community-view/2/"]').click()
		driver.find_element_by_xpath('//a [@href="/community_feed/2/"]').click()

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()