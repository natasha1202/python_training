import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, NoAlertPresentException


class TestAddGroups:

    def setup(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_path("//input[@value='Login']").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("abc")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("abcd")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("abcde")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()

    def is_element_presented(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False

    def is_alert_presented(self):
        try: self.wd.swith_to_alert()
        except NoAlertPresentException as e:
            return False

    def tear_down(self):
        self.wd.quit()
