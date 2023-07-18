import time
import unittest
from Base import SetUp
from Pages import SearchFlight

baseSetUp = SetUp.MyTestCase()


class FlightSearch(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.search = SearchFlight.SearchFlight(SetUp.driver)

    def setUp(self):
        baseSetUp.setUpClass()
        baseSetUp.agent_login()
        self.page_objects()

    def page_objects(self):
        self.search = SearchFlight.SearchFlight(SetUp.driver)

    def test_FlightPageAppear(self):
        self.search.goto_flights()
        time.sleep(3)
        pageTittle = SetUp.driver.title
        baseSetUp.check_result_string(pageTittle, "Search for best Flights")

    def test_AirportSelection(self):
        self.test_FlightPageAppear()
        actual_result = self.search.set_flying_from("Chattogram", "CTG_1")
        baseSetUp.check_result_string(actual_result, "CTG_1")

        actual_result = self.search.set_destination_to("Dhaka", "DHK-1")
        baseSetUp.check_result_string(actual_result, "DHK-1")

    def test_Calendar(self):
        self.test_FlightPageAppear()
        actual_result = self.search.set_depart_date("August 2023", "16")
        baseSetUp.check_result_string(actual_result, "16/8/23")

    def test_SearchFlightValid(self):
        self.test_FlightPageAppear()
        self.search.set_type("Economy")
        self.search.set_trip_travel("one")
        self.search.set_flying_from("Chattogram", "CTG_1")
        self.search.set_destination_to("Dhaka", "DHK-1")
        self.search.set_depart_date("August 2023", "16")
        self.search.set_travellers("adult", 2)
        self.search.set_type("Economy")
        self.search.click_search_button()
        time.sleep(2)
        self.search.click_select_flight()
        # pageTittle = SetUp.driver.title
        # baseSetUp.check_result_string(pageTittle, "Search Result")

    @classmethod
    def tearDownClass(cls):
        SetUp.driver.close()

    if __name__ == '__main__':
        unittest.main()
