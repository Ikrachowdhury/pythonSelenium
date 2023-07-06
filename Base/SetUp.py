from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages import LoginPage
import time
import unittest

driver = webdriver.Chrome()


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver.maximize_window()
        driver.implicitly_wait(500)
        driver.get("https://phptravels.net/admin/login.php")

    def setUp(self):
        log = LoginPage.Login(driver)
        log.set_password("demoadmin")
        log.set_mail("admin@phptravels.com")
        log.click_submit_button()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
