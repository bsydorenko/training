# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost:9000/")

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def creating_contact(self, wd):
        # add contacts
        wd.find_element_by_link_text("Додати контакт").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[1]").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("eee")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("sss")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("ddd")
        wd.find_element_by_name("submit").click()

    def logout(self, success, wd):
        # logout
        wd.find_element_by_link_text("Вийти").click()
        self.assertTrue(success)

    def test_test_add_contact(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.creating_contact(wd)
        self.logout(success, wd)


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
