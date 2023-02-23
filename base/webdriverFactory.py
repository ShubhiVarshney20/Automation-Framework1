from selenium import webdriver

class WebdriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def webdriverInstance(self):
        baseUrl = "https://courses.letskodeit.com/"
        if self.browser == "Chrome":
            driver = webdriver.Chrome()

        else:
            driver = webdriver.Edge()

        driver.get(baseUrl)
        driver.maximize_window()
        return driver

