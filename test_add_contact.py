# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group

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

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def creating_contact(self, wd, group):
        wd.find_element_by_link_text("Додати контакт").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[1]").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group.middle)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group.lastname)
        wd.find_element_by_name("submit").click()

    def logout(self, success, wd):
        wd.find_element_by_link_text("Вийти").click()
        self.assertTrue(success)

    def test_test_add_contact(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username = "admin", password = "secret")
        self.creating_contact(wd, Group(name="eee", middle="sss", lastname="ddd"))
        self.logout(success, wd)

    def test_test_add_empty_contact(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username = "admin", password = "secret")
        self.creating_contact(wd, Group(name="", middle="", lastname=""))
        self.logout(success, wd)


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
