import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class signup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url_basic = "http://172.17.0.1:7000/"

    def test_community_view(self):
        user = "root"
        pwd = "root1234"
	title = "Selenium Test Cases"
	delay = 20
        driver = webdriver.Firefox()
        driver.maximize_window()  # For maximizing window
        driver.get("http://172.17.0.1:7000/")
        driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
        driver.get("http://172.17.0.1:7000/login/?next=/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        driver.find_element_by_class_name('btn-block').click()
        driver.find_element_by_xpath('//a [@href="/communities/"]').click()
        driver.find_element_by_xpath('//a [@href="/community-view/1/"]').click()
	driver.find_element_by_xpath("/html/body/div[4]/ul/li[5]/a").click() # Group Content Tabbed Button
	driver.find_element_by_xpath("/html/body/div[4]/div/div[2]") # Checking For Text Under Group Content

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
