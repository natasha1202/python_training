# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest


class TestAddGroup:

    def test_add_group(self, driver):
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("abd")
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("abdc")
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("abdce")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_link_text("Logout").click()

    @staticmethod
    def is_element_present(driver, how, what):
        try: driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    @staticmethod
    def is_alert_present(driver):
        try: driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
