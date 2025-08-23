# -*- coding: utf-8 -*-
from contact import Contact


class TestAddContact:

    def test_add_contact(self, app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(first_name="aaa", last_name="bbb", mobile="89001111111",
                                             middle_name="", nickname="", title="", company="",
                                            address="", phone="", home="", work="", fax="", email="",
                                            email2="", email3="",homepage=""))
        app.logout()

