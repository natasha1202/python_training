import pytest
from selenium import webdriver
from fixture.application import Application


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get("http://localhost/addressbook/")
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def app(driver):
    application = Application(driver)
    return application
