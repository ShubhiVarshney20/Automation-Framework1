import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.login import Login
import unittest

@pytest.mark.usefixtures("setupDriver")
class Letskodeit_login(unittest.TestCase):
    @pytest.fixture(autouse= True)
    def setUpMethod(self, setupDriver):
        self.lp = Login(self.driver)
    def test_clickOnCourse(self):
        self.lp.logout()
        time.sleep(2)


