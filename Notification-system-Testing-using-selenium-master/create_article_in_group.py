__author__= 'Minali and Urmi'

'''
Article in a group can only be created by group_admin or by someone who is a member of the group.
(An user can become a member of the group by joining the group or by being added to the group by the group_admin)
Here group_admin is tester_notifications as he created the group

This script logins with tester_notifications and creates an article inside a group
'''

import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class create_env(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(command_executor='http://'+config('DOCKER_IP')+':'+config('DOCKER_PORT')+'/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)
		#self.driver = webdriver.Firefox()


	def test_create_article_in_group(self):
		driver = self.driver
		# Logging in by tester_notifications
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT')+"/login")
		elem = driver.find_element_by_id("id_username")
		user = config('NOTIFICATION_USER').split(',')
		elem.send_keys(user[0])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('NOTIFICATION_PASSWORD'))
		driver.find_element_by_class_name('btn-block').click()
		# Inside community
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT') + '/communities/')
		print (driver.current_url)
		driver.find_element_by_xpath('//a [@href="/community-view/' + config('NOTIFICATION_COMMUNITY_ID') + '/"]').click()
		print (driver.current_url)
		driver.find_element_by_xpath('//a [@href="/group-view/' + config('NOTIFICATION_GROUP_ID') + '/"]').click()
		print (driver.current_url)
		#driver.find_element_by_id("create_resource_id").click()
		#time.sleep(5)
		#driver.find_element_by_xpath("//button [@type='button' and @data-target='#modalCreate']").click()
		driver.find_element_by_xpath("//button [@type='button' and @data-target='#modalCreateArticlegrp']").click()
		driver.find_element_by_id("exampleCheck1").click()
		driver.find_element_by_id("create_group_article").click()
		title = driver.find_element_by_id("title")
		title.send_keys("TEST GROUP ARTICLE abc A")
		driver.find_element_by_id("next1").click()
		time.sleep(5)
		driver.find_element_by_id("next2").click()
		time.sleep(5)
		driver.find_element_by_id("finish").click()
		# Extracting the ARTICLE id
		var = driver.current_url
		article_id = var.split("/")[-2]
		f = open(".env","a")
		f.write("\nNOTIFICATION_GROUP_ARTICLE_ID="+article_id)
		f.close()

		

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()

