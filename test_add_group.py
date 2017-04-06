# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app():
    fixture = Application()
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="new_group", header="test1", footer="pass2"))
    app.logout()
    app.destroy()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
    app.destroy()
