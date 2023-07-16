import time
from selenium.webdriver import Keys
from Base import Util


def click_on_Flights():
    pass


class SearchFlight:
    def __init__(self, driver):
        self.search = None
        self.trip = None
        self.type = None
        self.Flight = None
        self.find = Util.ElementsUtil(driver)

    def goto_flights(self):
        self.Flight = self.find.element_by_xpath('//*[@id="navbarSupportedContent"]/div[1]/ul/li[1]/a')
        self.Flight.click()

    def dropdown(self, city, value, selector_box, selector_box_info):
        flying = self.find.element_by_xpath(selector_box)
        flying.click()
        flying_input = self.find.element_by_xpath(selector_box_info)
        flying_input.send_keys(city)
        time.sleep(6)
        flying_options = self.find.array_of_table("class", "select2-results__option")
        Flying = self.find.get_table_element(flying_options, value, "btn")
        Flying.click()
        time.sleep(5)

    def set_type(self, value):
        self.type = self.find.element_by_id("flight_type")
        self.type.click()
        time.sleep(2)
        self.find.dropdown(value, self.type)
        time.sleep(2)

    def set_trip_travel(self, value):
        if value == "one":
            self.trip = self.find.element_by_id("one-way")
            self.trip.click()

        elif value == "round":
            self.trip = self.find.element_by_id("round-trip")
            self.trip.click()
        time.sleep(3)

    def set_flying_from(self, city, value):
        self.dropdown(city, value, '//*[@id="onereturn"]/div[1]/div[1]/div[2]/span/span[1]/span',
                      '//*[@id="fadein"]/span/span/span[1]/input')

    def set_destination_to(self, city, value):
        self.dropdown(city, value, '//*[@id="onereturn"]/div[2]/div[2]/div[2]/span/span[1]/span',
                      '//*[@id="fadein"]/span/span/span[1]/input')

    def time(self, month_year, date):
        next = self.find.element_by_class("next")
        shown_month_year = self.find.element_by_class("switch").text
        while shown_month_year != month_year:
            next.click()
            shown_month_year = self.find.element_by_class("switch").text

        date_calender = self.find.array_of_table("class", "day")
        for i in range(len(date_calender)):
            shown_date = date_calender[i].text
            color = date_calender[i].value_of_css_property('color')
            if shown_date == date and color == "rgba(51, 51, 51, 1)":
                date_calender[i].click()
                break
        time.sleep(10)

    def set_depart_date(self, month_year, date):
        input_box = self.find.element_by_id("departure")
        input_box.click()
        self.time(month_year, date)

    def set_return_date(self, month_year, date):
        input_box = self.find.element_by_id("departure")
        input_box.click()
        self.time(month_year, date)

    def set_travellers(self, type, number):
        input_box = self.find.element_by_class("travellers")
        input_box.click()
        i = 1
        if type == "adult":
            while i != number:
                plus = self.find.element_by_xpath('//*[@id="onereturn"]/div[4]/div/div/div/div/div[1]/div/div/div[2]')
                plus.click()
                i += 1
        elif type == "child":
            while i != number:
                plus = self.find.element_by_xpath('//*[@id="onereturn"]/div[4]/div/div/div/div/div[2]/div/div/div[2]')
                plus.click()
                i += 1

        elif type == "infant":
            while i != number:
                plus = self.find.element_by_xpath('//*[@id="onereturn"]/div[4]/div/div/div/div/div[3]/div/div/div[2]')
                plus.click()
                i += 1
        time.sleep(5)

    def click_search_button(self):
        self.search = self.find.element_by_id("flights-search")
        self.search.click()


class SearchResult:
    def __init__(self, driver):
        self.find = Util.ElementsUtil(driver)
        pass

    def click_more_details(self):
        pass

    def click_select_flight(self):
        pass

