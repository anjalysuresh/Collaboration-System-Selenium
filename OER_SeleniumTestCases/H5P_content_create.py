__author__= 'Minali and Urmi'
import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class create_env(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(command_executor='http://'+config('DOCKER_IP')+':'+config('DOCKER_PORT')+'/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)
		#self.driver = webdriver.Firefox()


	def test_create_community(self):
		driver = self.driver
		# Logging in by admin
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('CONTENT_TOOLS_PORT')+"/login")
		elem = driver.find_element_by_id("id_username")
		user = config('CONTENT_TOOLS_USER').split(',')
		elem.send_keys(user[0])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('CONTENT_TOOLS_PASSWORD'))
		driver.find_element_by_class_name('btn-block').click()
		# Inside community
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('CONTENT_TOOLS_PORT') + '/communities/')
		print (driver.current_url)
		driver.find_element_by_xpath('//a [@href="/community-view/' + config('CONTENT_TOOLS_COMMUNITY_ID') + '/"]').click()
		#driver.find_element_by_id("create_resource_id").click()
		#time.sleep(5)
		#driver.find_element_by_xpath("//button [@type='button' and @data-target='#modalCreate']").click()
		driver.find_element_by_xpath("//button [@type='button' and @data-target='#modalCreate']").click()
		driver.find_element_by_xpath("//button [@type='button' and @data-target='#modalCreateh5p']").click()
		driver.find_element_by_id("exampleCheck4").click()
		driver.find_element_by_id("Yes").click()
		time.sleep(10)
		title = driver.find_element_by_id("id_title")
		title.send_keys("TEST h5p Content Tools abc")
		driver.find_element_by_id("id_h5p_type_0").click()
		time.sleep(10)
		driver.find_element_by_id("id_h5p_type_1").click()
		time.sleep(10)
		driver.find_element_by_id("submit_editor").click()
		
		

		

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()
