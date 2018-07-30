# __author__= 'rushikesh'
import unittest
from selenium import webdriver


class signup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url_basic = "http://172.17.0.1:7000/"

    def test_community_view(self):
        user = "root"
        pwd = "root1234"
        driver = webdriver.Firefox()
        driver.maximize_window()  # For maximizing window
        #driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
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
        driver.find_element_by_xpath("//button [@type='button' and @data-target='#modalCreate']").click()
	driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/button[4]").click() # Create Resource > Interactive Content Dialog Button
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[2]/div[6]/div/div/div[2]/form/div/div/input").click() # T and C Dialog Checkbox
	driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[2]/div[6]/div/div/div[3]/button[2]").click() # T and C Dialog Box Yes Button

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
