from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Base import Util
from selenium import webdriver


class Login:

    def __init__(self, driver):
        self.find = Util.ElementsUtil(driver)
        self.EmailField = self.find.element_by_id('email')
        self.PasswordField = self.find.element_by_id('password')
        self.SubmitButton = self.find.element_by_id('submit')

    def set_mail(self, email):
        self.EmailField.send_keys(email)

    def set_password(self, password):
        self.PasswordField.send_keys(password)

    def click_submit_button(self):
        self.SubmitButton.click()
