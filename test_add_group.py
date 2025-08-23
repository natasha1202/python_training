# -*- coding: utf-8 -*-
from group import Group


class TestAddGroup:

    def test_add_group(self, app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="abd", header="abdc", footer="abdce"))
        app.logout()

    def test_add_empty_group(self,app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()

