from selenium import webdriver

from Pages import LoginPage
import time
import unittest

driver = webdriver.Chrome()


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver.maximize_window()
        driver.implicitly_wait(500)

    def setUp(self):
        driver.get("https://phptravels.net/admin/login.php")
        log = LoginPage.Login(driver)
        log.set_password("demoadmin")
        log.set_mail("admin@phptravels.com")
        log.click_submit_button()
        time.sleep(10)

    def agent_login(self):
        driver.get("https://phptravels.net/login")
        log = LoginPage.Login(driver)
        log.set_password("demoagent")
        log.set_mail("agent@phptravels.com")
        log.click_login_button()
        time.sleep(10)

    def check_result_string(self, actual_result, expected):
        # print(actual_result)
        # print(expected)
        assert actual_result == expected


if __name__ == '__main__':
    unittest.main()
