import unittest
from selenium import webdriver
import requests
from decouple import config

class test(unittest.TestCase):

    def setUp(self):
        self.user = config("EVENT_LOGS_USER")
        self.pwd = config("EVENT_LOGS_PASSWORD")
        self.url_basic = "http://" + config("IP_ADDRESS") + ":" + config("EVENT_LOGS_PORT") + "/"
        self.token = config("EVENT_API_TOKEN")  #This should be generated by tester
        self.headers={'Authorization': 'Token ' + str(self.token)}
        print("Note that user should be a member of community that you select.")
        self.community_id = raw_input("Enter a community id: ")
        self.course_name = raw_input("Enter course name: ")

    def test_course_create(self):
        url_api = self.url_basic + 'logapi/event/course/create/'
        result = requests.get(url_api, headers = self.headers).json()
        new_result={}
        for key,value in result.iteritems():
            new_result[key.lower()] = value
        if(new_result["status code"] == 200):
            data = new_result["result"]
            total_hits = new_result["total hits"]

        driver = webdriver.Firefox()
        driver.maximize_window()  # For maximizing window
        driver.get(self.url_basic)
        driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(self.user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(self.pwd)
        driver.find_element_by_class_name('btn-block').click()
        driver.find_element_by_xpath('//a [@href="/communities/"]').click()
        driver.find_element_by_xpath('//a [@href="/community-view/' +  self.community_id + '/"]').click()
        driver.find_element_by_xpath("//button [@type='button' and @data-target='#modalCreate']").click()
        driver.find_element_by_xpath("//button [@type='button' and @data-target='#modalCreateCourse']").click()
        driver.find_element_by_id("exampleCheck3").click()
        driver.find_element_by_id("courseCreate").click()
        title = driver.find_element_by_id("name")
        title.send_keys(self.course_name)
        driver.find_element_by_id("course_create").click()

        url_api = self.url_basic + 'logapi/event/course/create/'
        result = requests.get(url_api, headers = self.headers).json()
        new_result={}
        for key,value in result.iteritems():
            new_result[key.lower()] = value
        if (new_result["status code"] == 200):
            data = new_result["result"]
            if (new_result["total hits"] == total_hits+ 1):
                self.assertEqual(data[0]["event_name"], "event.course.create")
                self.assertEqual(data[0]["event"]["community-id"], self.community_id)
                self.assertEqual(data[0]["event"]["course-name"], self.course_name)

        driver.quit()


if __name__ == '__main__':
    unittest.main()
