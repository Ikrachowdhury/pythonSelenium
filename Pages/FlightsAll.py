import time
from selenium.webdriver import Keys
from Base import Util


# dropdown error
class FlightView:

    def __init__(self, driver):

        self.ResetButton = None
        self.CheckboxAll = None
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

    def click_module_flight_status(self):
        module_status = self.find.element_by_xpath(
            "//tr[@class='modules_sort modules_flights type_flights']//input[@id='checkedbox']")
        status = module_status.get_attribute('data-status')
        # print(status)
        if status == "0":
            module_status.click()
            self.find.refresh()

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
        if len(self.TableArray) == 1:
            text = self.TableArray[0].text
            if text != "Entries not found.":
                return "ok"
            else:
                return "no"
        else:
            return "ok"

    def click_edit_button(self, buttonNumber):
        self.get_table()
        self.EditButton = self.find.get_table_element(self.TableArray, buttonNumber, 'xcrud-orange')
        self.EditButton.click()

    def get_EditFlight_identifier(self):
        pageStart = self.find.element_by_xpath(
            '/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[1]').text
        print(pageStart)
        return pageStart

    def click_satus(self, buttonNumber):
        entry = self.get_table()
        if entry == "ok":
            self.Status = self.find.get_table_element(self.TableArray, buttonNumber, 'updated_status')
            self.Status.click()
            return "ok"
        else:
            return "no"

    def click_delete_button(self, buttonNumber, value):
        entry = self.get_table()
        if entry == "ok":
            self.DeleteButton = self.find.get_table_element(self.TableArray, buttonNumber, 'xcrud-red')
            self.DeleteButton.click()
            time.sleep(3)
            self.find.alert_box(value)
            return "ok"
        else:
            return "no"

    def click_checkbox(self, buttonNumber):
        self.find.refresh()
        entry = self.get_table()
        if entry == "ok":
            self.Checkbox = self.find.get_table_element(self.TableArray, buttonNumber, 'checkboxcls')
            self.Checkbox.click()
            self.deleteAllBox = self.find.element_by_id("deleteAll")
            if self.deleteAllBox.is_displayed():
                return "deleteAll"
            else:
                return "error"
        else:
            return "no"

    def click_checkbox_all(self):

        self.CheckboxAll = self.find.element_by_id("select_all")
        self.CheckboxAll.click()
        self.deleteAllBox = self.find.element_by_id("deleteAll")
        if self.deleteAllBox.is_displayed():
            return "deleteAll"
        else:
            return "error"

    def click_delete_all(self, value):
        self.deleteAllBox.click()
        time.sleep(3)
        self.find.alert_box(value)
        time.sleep(3)
        self.get_table()
        table = self.TableArray
        return len(table)

    def click_search_button(self):
        self.SearchButton = self.find.element_by_xpath("/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/a")
        self.SearchButton.click()
        time.sleep(2)
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
        self.ResetButton = self.find.element_by_xpath(
            "/html/body/main/section/div[2]/div/div/div[1]/div[3]/span/span/span[4]/a[2]")
        return self.ResetButton.text

    def click_on_reset(self):
        self.ResetButton.click()
        time.sleep(3)
        self.AddButton = self.find.element_by_xpath("/html/body/main/section/div[2]/div/div/div[1]/div[1]/a")
        if self.AddButton.is_displayed():
            return "mainpage"
        else:
            return self.AddButton.text

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
        return self.find.driver.selector

    def get_first_element_from_table(self):
        self.get_table()
        id = self.find.get_table_element_xpath(self.TableArray, 0,
                                               '/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[4]/small')
        airline = self.find.get_table_element_xpath(self.TableArray, 0,
                                                    '/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[5]')
        from_airline = self.find.get_table_element_xpath(self.TableArray, 0,
                                                         '/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[6]')
        to_airline = self.find.get_table_element_xpath(self.TableArray, 0,
                                                       '/html/body/main/section/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[7]')
        return id.text, airline.text, from_airline.text, to_airline.text


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

    def time_box(self):
        hour = self.find.element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/dl/dd[2]/div/a')
        hour.click()
        self.find.element_action(hour)
        min = self.find.element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/dl/dd[3]/div/a')
        min.click()
        self.find.element_action(min)
        sec = self.find.element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/dl/dd[4]/div/a')
        sec.click()
        self.find.element_action(sec)

    def time(self, month_year, date, nxt, string):
        nexts = self.find.element_by_xpath(nxt)
        shown_month_year = self.find.element_by_xpath(string).text
        while shown_month_year != month_year:
            nexts.click()
            shown_month_year = self.find.element_by_xpath(string).text
            if shown_month_year == month_year:
                break

        date_calender = self.find.array_of_table("class", "day")
        for i in range(len(date_calender)):
            shown_date = date_calender[i].text
            # color = date_calender[i].value_of_css_property('color')
            if shown_date == date:
                date_calender[i].click()
                break
        time.sleep(5)
        self.Duration.click()

    def set_depart_date(self, month_year, date):
        self.DepartureTime.click()
        self.time(month_year, date, "//body/div[3]/div[1]/table[1]/thead[1]/tr[1]/th[3]//*[name()='svg']",
                  "//body/div[3]/div[1]/table[1]/thead[1]/tr[1]/th[2]")

    def set_arrive_date(self, month_year, date):
        self.ArrivalTime.click()
        self.time(month_year, date, "//body/div[4]/div[1]/table[1]/thead[1]/tr[1]/th[3]//*[name()='svg']",
                  "//body/div[4]/div[1]/table[1]/thead[1]/tr[1]/th[2]")

    def set_departure_time(self):
        self.DepartureTime.click()
        self.time_box()

    def set_arrival_time(self):
        self.ArrivalTime.click()
        self.time_box()

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
        self.ResetButton.click()
        time.sleep(3)
        self.AddButton = self.find.element_by_xpath("/html/body/main/section/div[2]/div/div/div[1]/div[1]/a")
        if self.AddButton.is_displayed():
            return "mainpage"
        else:
            return self.AddButton.text


class FlightEdit(FlightAdd):
    def __init__(self, driver):
        super().__init__(driver)
        self.AirportString = None
        self.Airport = None
        self.ArrivalTimeR = None
        self.DepartureTimeR = None
        self.DurationR = None
        self.Save = None
        self.Add = None
        self.ExportInToCVS = None

    def click_export(self):
        self.find.scroll_to(self.ExportInToCVS)
        self.ExportInToCVS = self.find.element_by_xpath('//*[@id="xcrud-ajax-fk89nm"]/div[1]/a[1]')
        self.ExportInToCVS.click()
        link = self.find.switch_to_window()
        return link

    def click_add_route(self):
        self.find.scroll_to(self.Add)
        self.Add = self.find.element_by_xpath(
            '//*[@id="xcrud-ajax-fk89nm"]/div[1]/a[2]')
        self.Add.click()
        self.Airport = self.find.element_by_xpath(
            '// *[ @ id = "xcrud-ajax-i0mkrn"] / div[2] / table / tbody / tr[1] / td[2] / span / span[1] / span')
        self.ArrivalTimeR = self.find.element_by_name("ZmxpZ2h0c19yb3V0ZXMuYXJyaXZhbF90aW1l")
        self.DepartureTimeR = self.find.element_by_name("ZmxpZ2h0c19yb3V0ZXMuZGVwYXJ0dXJlX3RpbWU-")
        self.DurationR = self.find.element_by_xpath('//*[@id="xcrud-ajax-i0mkrn"]/div[2]/table/tbody/tr[4]/td[2]/input')
        self.AirportString = self.find.element_by_xpath('//*[@id="xcrud-ajax-i0mkrn"]/div[2]/table/tbody/tr[1]/td[1]')
        return self.AirportString

    def set_airport_route(self, value):
        self.Airport.click()
        self.select_option(value, "/html/body/span/span/span[1]/input")

    def set_arrival_time_route(self, value):
        self.ArrivalTimeR.send_keys(value)
        self.time_box()

    def set_departure_time_route(self, value):
        self.Airport.click()
        self.time_box()

    def set_duration_route(self, value):
        self.DepartureTimeR.send_keys(value)
        self.time_box()

    def click_on_save_route(self):
        self.Save = self.find.element_by_xpath('//*[@id="xcrud-ajax-i0mkrn"]/div[1]/a[1]')
        self.Save.click()
