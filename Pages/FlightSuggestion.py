import time
from selenium.webdriver import Keys
from Base import Util


class FlightSuggestionView:
    def __init__(self, driver):
        self.find = Util.ElementsUtil(driver)
        self.TableArray = None
        self.AddButton = None
        self.Status = None
        self.EditButton = None
        self.DeleteButton = None
        self.Checkbox = None
        self.CheckboxAll = None
        self.deleteAllBox = None
        self.SearchButton = None
        self.DropBoxName = None
        self.SearchInputBox = None
        self.GoButton = None
        self.ResetButton = None
        self.PopUpBox = None

    def click_module_flight_status(self):
        module_status = self.find.element_by_xpath(
            "//tr[@class='modules_sort modules_flights type_flights']//input[@id='checkedbox']")
        status = module_status.get_attribute('data-status')
        # print(status)
        if status == "0":
            module_status.click()
            self.find.refresh()

    def get_table(self):
        self.TableArray = self.find.array_of_table("class", "xcrud-row")

    def click_Add_button(self):
        self.AddButton = self.find.element_by_xpath("/html/body/main/section/div[2]/div/div/div[1]/div[1]/a")
        self.AddButton.click()
        time.sleep(2)
        page_indicator = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[1]")
        return page_indicator.text

    def click_satus(self, buttonNumber):
        self.get_table()
        self.Status = self.find.get_table_element(self.TableArray, buttonNumber, 'updated_status')
        self.Status.click()

    def click_delete_button(self, buttonNumber, value):
        self.get_table()
        self.DeleteButton = self.find.get_table_element(self.TableArray, buttonNumber, 'xcrud-red')
        self.DeleteButton.click()
        time.sleep(3)
        self.find.alert_box(value)

    def click_checkbox(self, buttonNumber):
        self.get_table()
        self.Checkbox = self.find.get_table_element(self.TableArray, buttonNumber, 'checkboxcls')
        self.Checkbox.click()
        self.deleteAllBox = self.find.element_by_id("deleteAll")
        if self.deleteAllBox.is_displayed():
            return "deleteAll"
        else:
            return "error"

    def click_checkbox_all(self):

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
        self.find.scroll_bottom()
        self.SearchButton = self.find.element_by_class("xcrud-search-toggle")
        self.SearchButton.click()
        time.sleep(2)
        self.GoButton = self.find.element_by_xpath(
            '/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[4]/a')
        return self.GoButton.text

    def dropdown(self, value, selector_box, selector_box_info):
        self.DropBoxName = self.find.element_by_xpath(selector_box)
        self.DropBoxName.click()
        DropboxOptions = self.find.element_by_xpath(selector_box_info)
        DropboxOptions.send_keys(value)
        DropboxOptions.send_keys(Keys.ENTER)

    def set_field_dropbox(self, value):
        self.dropdown(value,
                      "/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[3]/span[1]/span",
                      "/html/body/span/span/span[1]/input")

    def set_type_dropbox(self, value):
        self.dropdown(value,
                      "/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[2]/span[1]/span",
                      "/html/body/span/span/span[1]/input")

    def set_no_dropBox(self, value):
        self.dropdown(value,
                      "/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[1]/span[1]/span",
                      "/html/body/span/span/span[1]/input")

    def set_input_box(self, value):
        self.SearchInputBox = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/input")
        self.SearchInputBox.send_keys(value)

    def click_on_go(self):
        self.GoButton = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[4]/a")
        self.GoButton.click()
        time.sleep(2)
        self.ResetButton = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[4]/a[2]")
        if self.ResetButton.is_displayed():
            return self.ResetButton.text
        else:
            return "error"

    def click_on_reset(self):
        self.ResetButton.click()
        time.sleep(3)
        self.AddButton = self.find.element_by_xpath("/html/body/main/section/div[2]/div/div/div[1]/div[1]/a")
        if self.AddButton.is_displayed():
            return "mainpage"
        else:
            return self.AddButton.text

    def get_text_popup(self):
        self.PopUpBox = self.find.element_by_xpath("/html/body/div[2]/div[1]/div[2]/div")
        return self.PopUpBox.text

    def get_first_element_from_table(self):
        self.get_table()
        type = self.find.get_table_element_xpath(self.TableArray, 0,
                                                 '/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[4]')
        city_airport = self.find.get_table_element_xpath(self.TableArray, 0,
                                                         '/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[5]')
        return type.text, city_airport.text


class AddFlightSuggestion:
    def __init__(self, driver):
        self.find = Util.ElementsUtil(driver)
        self.DropBoxName = None
        self.Order = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/input")
        self.Save = self.find.element_by_xpath("/html/body/main/section/div[2]/div/div/div[1]/div[1]/a[1]")
        self.Return = self.find.element_by_xpath("/html/body/main/section/div[2]/div/div/div[1]/div[1]/a[2]")

    def dropdown(self, value, selector_box, selector_box_info):
        self.DropBoxName = self.find.element_by_xpath(selector_box)
        self.DropBoxName.click()
        DropboxOptions = self.find.element_by_xpath(selector_box_info)
        DropboxOptions.send_keys(value)
        DropboxOptions.send_keys(Keys.ENTER)

    def set_status(self, value):
        self.dropdown(value,
                      "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span/span[1]/span",
                      "/html/body/span/span/span[1]/input")

    def set_type(self, value):
        self.dropdown(value,
                      "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/span/span[1]/span",
                      "/html/body/span/span/span[1]/input")

    def set_city_airport(self, value):
        self.dropdown(value,
                      "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[2]/span/span[1]/span",
                      "/html/body/span/span/span[1]/input")
        pass

    def set_order(self, value):
        self.Order.click()
        self.Order.send_keys(value)

    def click_on_save(self):
        self.Save.click()

    def click_on_return(self):
        self.Return.click()

    def check_return_page(self, add_button):
        if add_button.is_displayed():
            return "correct page"
        else:
            return "error"

    def get_first_element_from_table(self, table):
        type = self.find.get_table_element_xpath(table, 0,
                                                 '/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[4]')
        city_airport = self.find.get_table_element(table, 0,
                                                   '//html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[5]')
        return type.text, " ", city_airport.text
