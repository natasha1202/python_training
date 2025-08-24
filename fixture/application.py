from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, driver):
        self.wd = driver
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def go_to_homepage(self):
        self.wd.find_element_by_xpath(".//a[contains(@href, './')]").click()


