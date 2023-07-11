import time
from selenium.webdriver import Keys
from Base import Util


class FlightBookings:
    def __init__(self, driver):
        self.find = Util.ElementsUtil(driver)
        self.edit_no = None
        self.TableArray = None
        self.ViewInvoice = None
        self.Checkbox = None
        self.CheckboxAll = None
        self.deleteAllBox = None
        self.SearchButton = None
        self.DropBoxName = None
        self.SearchInputBox = None
        self.GoButton = None
        self.ResetButton = None
        self.PopUpBox = None
        self.Back = None

    def get_table(self):
        self.TableArray = self.find.array_of_table("class", "xcrud-row")

    def click_view_invoice_button(self, buttonNumber):
        self.get_table()
        self.ViewInvoice = self.find.get_table_element(self.TableArray, buttonNumber, 'xcrud-button')
        self.ViewInvoice.click()
        return self.find.driver.tittle

    def click_checkbox(self, buttonNumber):
        self.get_table()
        self.Checkbox = self.find.get_table_element(self.TableArray, buttonNumber, 'checkboxcls')
        self.Checkbox.click()
        self.deleteAllBox = self.find.element_by_id("deleteAll")
        if self.deleteAllBox.is_displayed():
            return "deleteAll"
        else:
            return "error"

    def click_checkbox_all(self, buttonNumber):

        self.CheckboxAll = self.find.element_by_id("select_all")
        self.Checkbox.click()
        self.deleteAllBox = self.find.element_by_id("deleteAll")
        if self.deleteAllBox.is_displayed():
            return "deleteAll"
        else:
            return "error"

    def click_delete_all(self, value):
        self.deleteAllBox.click()
        self.find.alert_box(value)

    def click_search_button(self):
        self.SearchButton = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div[2]/div/div[1]/div[3]/span/a")
        self.SearchButton.click()
        self.GoButton = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div[2]/div/div[1]/div[3]/span/span/span[4]/a")

        return self.GoButton.text

    def dropdown(self, value, selector_box, selector_box_info):
        self.DropBoxName = self.find.element_by_xpath(selector_box)
        self.DropBoxName.click()
        DropboxOptions = self.find.element_by_xpath(selector_box_info)
        DropboxOptions.send_keys(value)
        DropboxOptions.send_keys(Keys.ENTER)

    def set_field(self, value):
        self.dropdown(value,
                      "/html/body/main/section/div[2]/div/div[2]/div/div[1]/div[3]/span/span/span[3]/span[1]/span",
                      "/html/body/span/span/span[1]/input")

    def set_payment_status(self, value):
        self.dropdown(value,
                      "/html/body/main/section/div[2]/div/div[2]/div/div[1]/div[3]/span/span/span[2]/span[1]/span",
                      "/html/body/span/span/span[1]/input")

    def set_booking_status(self, value):
        self.dropdown(value,
                      "/html/body/main/section/div[2]/div/div[2]/div/div[1]/div[3]/span/span/span[1]/span[1]/span",
                      "/html/body/span/span/span[1]/input")

    def set_input_box(self, value):
        self.SearchInputBox = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div[2]/div/div[1]/div[3]/span/span/input")
        self.SearchInputBox.send_keys(value)

    def click_on_go(self):
        self.GoButton = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div[2]/div/div[1]/div[3]/span/span/span[4]/a")
        self.GoButton.click()
        time.sleep(2)
        self.ResetButton = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div[2]/div/div[1]/div[3]/span/span/span[4]/a[2]")
        if self.ResetButton.is_displayed():
            return self.ResetButton.text
        else:
            return "error"

    def click_on_reset(self):
        self.ResetButton.click()
        if self.ResetButton.is_displayed():
            return self.ResetButton.text
        else:
            return "mainpage"

    def click_back_button(self):
        self.Back = self.find.element_by_xpath("/html/body/main/section/div[1]/div/div[2]/a")
        self.Back.click()
        time.sleep(5)
        return self.find.driver.tittle

    def get_text_popup(self):
        self.PopUpBox = self.find.element_by_xpath("/html/body/div[2]/div[1]/div[2]/div")
        return self.PopUpBox.text

    def get_first_flight_from_table(self):
        self.get_table()
        username = self.find.get_table_element(self.TableArray, 0, 'fw-light')
        return username.text
