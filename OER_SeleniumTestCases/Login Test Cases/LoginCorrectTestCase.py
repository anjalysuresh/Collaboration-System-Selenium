#!/usr/bin/env python

import unittest
from selenium import webdriver

class LoginCorrect(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_LoginCorrect(self):
        user ="root"
        pwd= "root1234"
        driver = webdriver.Firefox()
        driver.get("http://172.17.0.1:7000/login")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        driver.find_element_by_class_name('btn-block').click()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
        unittest.main()
