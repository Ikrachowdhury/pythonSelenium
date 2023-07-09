import time

from selenium.webdriver import Keys

from Base import Util


# dropdown error
class FlightView:

    def __init__(self, driver):

        self.find = Util.ElementsUtil(driver)
        self.edit_no = None
        self.TableArray = None
        self.EditButton = None
        self.edit_no = None
        self.DeleteButton = None
        self.Status = None
        self.Checkbox = None
        self.deleteAllBox = None
        self.AddButton = None
        self.SearchButton = None
        self.FieldDropbox = None
        self.TypeDropbox = None
        self.NumberDropbox = None
        self.SearchInputBox = None
        self.GoButton = None
        self.PopUpBox = None
        self.GoButton = None
        self.Back = None

    def click_add_button(self):
        self.AddButton = self.find.element_by_xpath("html/body/main/section/div[2]/div/div/div[1]/div[1]")
        self.AddButton.click()

    def get_AddFlight_identifier(self):
        pageStart = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[1]").text
        print(pageStart)
        return pageStart

    def set_field_dropdown(self, value):
        self.FieldDropbox = self.find.element_by_id("select2-column-sg-container")
        self.find.dropdown(value, self.FieldDropbox)

    def get_table(self):
        self.TableArray = self.find.array_of_table("class", "xcrud-row")

    def click_edit_button(self, buttonNumber):
        self.get_table()
        self.EditButton = self.find.get_table_element(self.TableArray, buttonNumber, 'xcrud-orange')
        self.EditButton.click()

    def get_EditFlight_identifier(self):
        pageStart = self.find.element_by_xpath(
            '/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[1]').text
        print(pageStart)
        return pageStart

    def click_delete_button(self, buttonNumber):
        self.get_table()
        self.DeleteButton = self.find.get_table_element(self.TableArray, buttonNumber, 'xcrud-red')

    def click_satus(self, buttonNumber):
        self.get_table()
        self.Status = self.find.get_table_element(self.TableArray, buttonNumber, 'updated_status')
        self.Status.click()

    def click_checkbox(self, buttonNumber):
        self.get_table()
        self.Checkbox = self.find.get_table_element(self.TableArray, buttonNumber, 'checkboxcls')
        self.Checkbox.click()
        self.deleteAllBox = self.find.element_by_id("deleteAll")
        if self.deleteAllBox.is_displayed():
            return "deleteAll"
        else:
            return "error"

    def click_delete_all(self):
        self.deleteAllBox.click()


    def click_search_button(self):
        self.SearchButton = self.find.element_by_xpath("/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/a")
        self.SearchButton.click()
        self.GoButton = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[4]/a")
        return self.GoButton.text

    def set_field_dropdown(self, value):
        self.FieldDropbox = self.find.element_by_xpath(
            '/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[3]/span[1]/span')
        self.FieldDropbox.click()
        FieldDropboxOptions = self.find.element_by_xpath("/html/body/span/span/span[1]/input")
        FieldDropboxOptions.send_keys(value)
        FieldDropboxOptions.send_keys(Keys.ENTER)

    def set_type_box(self, value):
        self.TypeDropbox = self.find.element_by_xpath(
            '/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[2]/span[1]/span')
        self.TypeDropbox.click()
        TypedDropboxOptions = self.find.element_by_xpath('/html/body/span/span/span[1]/input')
        TypedDropboxOptions.send_keys(value)
        TypedDropboxOptions.send_keys(Keys.ENTER)

    def set_no_drop_box(self, value):
        self.NumberDropbox = self.find.element_by_xpath(
            '/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[1]/span[1]/span')
        self.NumberDropbox.click()
        noDropboxOptions = self.find.element_by_xpath('/html/body/span/span/span[1]/input')
        noDropboxOptions.send_keys(value)
        noDropboxOptions.send_keys(Keys.ENTER)

    def click_on_go(self):
        self.GoButton = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[4]/a")
        self.GoButton.click()
        time.sleep(2)
        resetButton = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[4]/a[2]")
        return resetButton.text

    def set_input_box(self, value):
        self.SearchInputBox = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/input")
        self.SearchInputBox.send_keys(value)

    def get_text_popup(self):
        self.PopUpBox = self.find.element_by_xpath("/html/body/div[2]/div[1]/div[2]/div")
        return self.PopUpBox.text

    def click_back_button(self):
        self.Back = self.find.element_by_xpath("/html/body/main/section/div[1]/div/div[2]/a")
        self.Back.click()
        time.sleep(5)
        return self.find.driver.tittle



class FlightAdd:
    pass


class FlightEdit:
    pass
