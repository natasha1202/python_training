# -*- coding: utf-8 -*-
from contact import Contact
from group import Group


class TestAddGroup:

    def test_add_group(self, app, driver):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="abd", header="abdc", footer="abdce"))
        self.app.logout()

    def test_add_empty_group(self,app, driver):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def test_add_contact(self, app, driver):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(driver, Contact(first_name="aaa", last_name="bbb", mobile="89001111111",
                                             middle_name="", nickname="", title="", company="",
                                            address="", phone="", home="", work="", fax="", email="",
                                            email2="", email3="",homepage=""
                                            ))
        self.app.logout()

