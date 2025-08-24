# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="aaa", last_name="bbb", mobile="89001111111",
                               middle_name="", nickname="", title="", company="",
                               address="", phone="", home="", work="", fax="", email="",
                               email2="", email3="", homepage=""))
    app.session.logout()
