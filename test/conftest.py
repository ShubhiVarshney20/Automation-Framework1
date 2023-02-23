import pytest
from pages.login import Login
from selenium import webdriver
from base.webdriverFactory import WebdriverFactory

@pytest.fixture(scope= "class")
def setupDriver(request, browser):
    wdf = WebdriverFactory(browser)
    driver = wdf.webdriverInstance()
    lg = Login(driver)
    lg.loginLetsKodeit("shubhi.varshney@cloudanalogy.com", "shubhi@cloud22")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print("This is the end of class")
    driver.quit



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope= "session")
def browser(request):
    return request.config.getoption("--browser")

