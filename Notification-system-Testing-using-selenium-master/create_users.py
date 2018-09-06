__author__= 'Minali and Urmi'
import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class create_env(unittest.TestCase):

	def setUp(self):
		
                self.driver = webdriver.Remote(command_executor='http://'+config('DOCKER_IP')+':'+config('DOCKER_PORT')+'/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
	
	def create_user(self,username,email,password):
		driver = self.driver
		
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT')+"/signup")
		password_confirmation= password
		elem = driver.find_element_by_id("username")
		elem.send_keys(username)
		elem = driver.find_element_by_id("email")
		elem.send_keys(email)
		elem = driver.find_element_by_id("password1")
		elem.send_keys(password)
		elem = driver.find_element_by_id("password2")
		elem.send_keys(password_confirmation)
		driver.find_element_by_id('submit').click()

	def test_create_users(self):
		driver = self.driver
		user = config('NOTIFICATION_USER').split(',')
		password = config('NOTIFICATION_PASSWORD')
		email = "@gmail.com"
		self.create_user(user[0],user[0]+email,password)
		self.create_user(user[1],user[1]+email,password)
		self.create_user(user[2],user[2]+email,password)
		self.create_user(user[4],user[4]+email,password)


	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()
