import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from decouple import config
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


class contenttools(unittest.TestCase):

    def setUp(self):
      self.driver = webdriver.Remote(command_executor='http://'+config('DOCKER_IP')+':'+config('DOCKER_PORT')+'/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)

    def login(self,var):
      driver = self.driver
      driver.get("http://" + config('IP_ADDRESS')+ ":" + config('CONTENT_TOOLS_PORT'))
      driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
      driver.get("http://" + config('IP_ADDRESS') + ":" + config('CONTENT_TOOLS_PORT') + '/login/?next=/')
      elem = driver.find_element_by_id("id_username")
      user = config('CONTENT_TOOLS_USER').split(',')
      elem.send_keys(user[var])
      elem = driver.find_element_by_id("id_password")
      elem.send_keys(config('CONTENT_TOOLS_PASSWORD'))
      driver.find_element_by_class_name('btn-block').click()
      
    def test_deleteArticle(self):
      driver = self.driver
      self.login(0) # logging in with tester_contenttools who is the creater of the article
      driver.get("http://" + config('IP_ADDRESS') + ":" + config('CONTENT_TOOLS_PORT') + '/mydashboard/')
      driver.print(driver.current_url)
      driver.sleep(5)
      driver.find_element_by_xpath('//a [@href="/article-view/' + config('CONTENT_TOOLS_ARTICLE_ID') + '/"]').click()
      print(driver.current_url)
      driver.find_element_by_xpath('//a [@href="/article-edit/' + config('CONTENT_TOOLS_ARTICLE_ID') + '/"]').click()
      driver.find_element_by_xpath('//a [@href="/article-delete/' + config('CONTENT_TOOLS_ARTICLE_ID') + '/"]').click()
      print (driver.current_url)
      driver.find_element_by_class_name('btn-danger').click()

    def tearDown(self):
      self.driver.quit()


if __name__ == '__main__':
    unittest.main()
