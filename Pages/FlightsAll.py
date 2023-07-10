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

    def get_first_flight_from_table(self):
        self.get_table()
        username = self.find.get_table_element(self.TableArray, 0, 'fw-light')
        return username.text


class FlightAdd:
    def __init__(self, driver):
        self.find = Util.ElementsUtil(driver)
        self.Status = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span/span[1]/span")
        self.User_id = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/span/span[1]/span")
        self.Airline = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[2]/span/span[1]/span")
        self.AirportTo = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[5]/td[2]/span/span[1]/span")
        self.AirportFrom = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/span/span[1]/span")
        self.AdultPrice = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[6]/td[2]/input")
        self.ChildPrice = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[7]/td[2]/input")
        self.InfintPrice = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[8]/td[2]/input")
        self.Duration = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[9]/td[2]/input")
        self.DepartureTime = self.find.element_by_name("ZmxpZ2h0cy5kZXBhcnR1cmVfdGltZQ--")
        self.ArrivalTime = self.find.element_by_name("ZmxpZ2h0cy5hcnJpdmFsX3RpbWU-")
        self.Baggage = self.find.element_by_xpath(
            '/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[12]/td[2]/input')
        self.CabinBagage = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[13]/td[2]/input")
        self.Type = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[14]/td[2]/span/span[1]/span")
        self.Refundable = self.find.element_by_xpath(
            '/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[15]/td[2]/div/span/span[1]/span')
        self.Save = self.find.element_by_xpath('/html/body/main/section/div[2]/div/div/div[1]/div[1]/a[1]')
        self.Return = self.find.element_by_xpath("/html/body/main/section/div[2]/div/div/div[1]/div[1]/a[2]")

    def select_option(self, value, selector):
        Options = self.find.element_by_xpath(selector)
        Options.send_keys(value)
        Options.send_keys(Keys.ENTER)

    def set_status(self, value):
        self.Status.click()
        self.select_option(value, "/html/body/span/span/span[1]/input")

    def set_id(self, value):
        self.User_id.click()
        self.select_option(value, "/html/body/span/span/span[1]/input")

    def set_airline(self, value):
        self.Airline.click()
        self.select_option(value, "/html/body/span/span/span[1]/input")

    def set_airport_from(self, value):
        self.AirportFrom.click()
        self.select_option(value, "/html/body/span/span/span[1]/input")

    def set_airport_to(self, value):
        self.AirportTo.click()
        self.select_option(value, "/html/body/span/span/span[1]/input")

    def set_adult_price(self, value):
        self.AdultPrice.send_keys(value)

    def set_child_price(self, value):
        self.ChildPrice.send_keys(value)

    def set_infant_price(self, value):
        self.InfintPrice.send_keys(value)

    def set_duration(self, value):
        self.Duration.click()
        self.Duration.send_keys(value)

    def set_departure_time(self):
        self.DepartureTime.click()
        hour = self.find.element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/dl/dd[2]/div/a')
        hour.click()
        self.find.element_action(hour)
        min = self.find.element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/dl/dd[3]/div/a')
        min.click()
        self.find.element_action(min)
        sec = self.find.element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/dl/dd[4]/div/a')
        sec.click()
        self.find.element_action(sec)

    def set_arrival_time(self):
        self.ArrivalTime.click()
        hour = self.find.element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/dl/dd[2]/div/a')
        hour.click()
        self.find.element_action(hour)
        min = self.find.element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/dl/dd[3]/div/a')
        min.click()
        self.find.element_action(min)
        sec = self.find.element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/dl/dd[4]/div/a')
        sec.click()
        self.find.element_action(sec)

    def set_baggage(self, value):
        self.Baggage.click()
        self.Baggage.send_keys(value)

    def set_cabin_baggage(self, value):
        self.CabinBagage.click()
        self.CabinBagage.send_keys(value)

    def set_type(self, value):
        self.Type.click()
        self.select_option(value, "/html/body/span/span/span[1]/input")

    def set_refundable(self, value):
        self.Refundable.click()
        self.select_option(value, "/html/body/span/span/span[1]/input")

    def click_on_save(self):
        self.find.scroll_to(self.Status)
        time.sleep(5)
        self.Save.click()

    def click_on_return(self):
        self.Return.click()


class FlightEdit(FlightAdd):
    def __init__(self, driver):
        super().__init__(driver)
        self.Airport = None
        self.ArrivalTimeR = None
        self.DepartureTimeR = None
        self.DurationR = None
        self.Save = None
        self.Add = self.find.element_by_xpath(
            '//*[@id="xcrud-ajax-fk89nm"]/div[1]/a[2]')
        self.ExportInToCVS = self.find.element_by_xpath('//*[@id="xcrud-ajax-fk89nm"]/div[1]/a[1]')

    def click_export(self):
        self.find.scroll_to(self.ExportInToCVS)
        self.ExportInToCVS.click()

    def click_add_route(self):
        self.ExportInToCVS.click()
        pass

    def set_airport_route(self, value):
        pass

    def set_arraival_time_route(self, value):
        pass

    def set_departure_time_route(self, value):
        pass

    def duration_rooute(self, value):
        pass

    def click_on_save(self):
        pass

    def click_on_return(self):
        pass
