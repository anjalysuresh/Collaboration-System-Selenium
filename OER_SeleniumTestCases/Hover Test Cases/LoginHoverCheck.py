#!/usr/bin/env python

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os

class LoginCorrect(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
	self.driver.maximize_window()

    def test_LoginHover(self):
        self.driver.get("http://172.17.0.1:7000")
	element_to_hover_over = self.driver.find_element_by_xpath('//a[@href="/login/?next=/"]')
	hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
	hover.perform()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
        unittest.main()
