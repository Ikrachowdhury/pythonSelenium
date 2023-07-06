
from Base import Util

#dropdown error
class FlightView:
    # xcrud-row =classname table box
    # /html/body/main/section/div[2]/div/div/div[1]/div[1]=xpath add button
    # /html/body/main/section/div[2]/div/div/div[1]/div[3]/span/a=xpath search button
    # /html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/input= searchbox
    # /html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[1]/span[1]/span=dropdownbox 1
    # select2-phrase-va-container=Id dropdown 2 economy
    # select2-column-sg-container=Id dropdown 3 all files
    # /html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[4]/a=go button xpath
    # xcrud-orange=classname edit button
    # xcrud-red=classname delete  button
    def __init__(self, driver):
        self.find = Util.ElementsUtil(driver)
        self.edit_no = None
        self.TableArray = None
        self.EditButton = None
        self.edit_no = None
        self.DeleteButton = None
        self.Status = None
        self.Checkbox = None
        self.AddButton = None
        self.SearchButton = None
        self.FieldDropbox = None
        self.TypeDropbox = None
        self.NumberDropbox = None
        self.SearchInputBox = None

    def click_add_button(self):
        self.AddButton = self.find.element_by_xpath("html/body/main/section/div[2]/div/div/div[1]/div[1]")
        self.AddButton.click()

    def get_table(self):
        self.TableArray = self.find.array_of_table("class", "xcrud-row")

    def click_edit_button(self, buttonNumber):
        self.get_table()
        self.EditButton = self.find.get_table_element(self.TableArray, buttonNumber, 'xcrud-orange')
        self.EditButton.click()

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

    def click_search_button(self):
        self.SearchButton = self.find.element_by_xpath("/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/a")
        self.SearchButton.click()

    def set_field_dropdown(self, value):
        self.FieldDropbox = self.find.element_by_id("select2-column-sg-container")
        self.find.dropdown(value,self.FieldDropbox)

        pass

    def set_type_dropdown(self, value):
        pass

    def set_no_drop_box(self, value):
        pass

    def set_no_drop_box(self, value):
        pass

    def set_input_box(self, value):
        pass


class FlightAdd:
    pass


class FlightEdit:
    pass
