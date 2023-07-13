import time
from selenium.webdriver import Keys
from Base import Util


def click_on_Flights():
    pass


class SearchFlight:
    def __init__(self, driver):
        self.Flying = None
        self.trip = None
        self.type = None
        self.DropBoxName = None
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

    def set_depart_date(self,month_year,date):
        input_box = self.find.element_by_id("departure")
        input_box.click()
        month_year_provided =

        pass

    def set_return_date(self):

        pass

    def set_travellers(self):
        pass

    def click_search_button(self):
        pass


class SearchResult:
    def __init__(self, driver):
        self.find = Util.ElementsUtil(driver)
        pass

    def click_more_details(self):
        pass

    def click_select_flight(self):
        pass

    def check_more_details_load(self):
        pass
