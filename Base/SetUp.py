import traceback

from selenium import webdriver

from Pages import LoginPage
import time
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(500)

    def admin_login(self):
        self.driver.get("https://phptravels.net/admin/login.php")
        log = LoginPage.Login(self.driver)
        log.set_password("demoadmin")
        log.set_mail("admin@phptravels.com")
        log.click_submit_button()
        time.sleep(10)

    def agent_login(self):
        self.driver.get("https://phptravels.net/login")
        log = LoginPage.Login(self.driver)
        log.set_password("demoagent")
        log.set_mail("agent@phptravels.com")
        log.click_login_button()
        time.sleep(10)

    def check_result_string(self, actual_result, expected):
        # print(actual_result)
        # print(expected)
        try:
            assert actual_result == expected
        except Exception:
            file_name = 'screenshot.png'
            self.driver.get_screenshot_as_file(file_name)
            traceback.print_exc()


if __name__ == '__main__':
    unittest.main()
