from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Base import Util
from selenium import webdriver


class Login:

    def __init__(self, driver):
        self.find = Util.ElementsUtil(driver)
        self.EmailField = self.find.element_by_id('email')
        self.PasswordField = self.find.element_by_id('password')
        self.SubmitButton = None
        self.LogInButton = None

    def set_mail(self, email):
        self.EmailField.send_keys(email)

    def set_password(self, password):
        self.PasswordField.send_keys(password)

    def click_submit_button(self):
        self.SubmitButton = self.find.element_by_id('submit')
        self.SubmitButton.click()

    def click_login_button(self):
        self.LogInButton = self.find.element_by_id('submitBTN')
        self.LogInButton.click()
