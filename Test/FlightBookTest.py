import time
import unittest
from Base import SetUp
from Test import SearchFlightTest
from Pages import FlightsBooking, SearchFlight

baseSetUp = SetUp.MyTestCase()


class FlightSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        baseSetUp.setUp()
        baseSetUp.agent_login()

    def setUp(self):
        self.page_objects()

    def page_objects(self):
        self.search = SearchFlight.SearchFlight(baseSetUp.driver)
        self.booking = FlightsBooking.BookFlight(baseSetUp.driver)

    def set_value(self):
        self.booking.set_title("Miss")
        self.booking.set_first_name("Ikra")
        self.booking.set_last_name("Chy")
        self.booking.set_nationality_traveller("Bangladesh")
        self.booking.set_nid("012345678901234")
        self.booking.set_payment_method("paypal")
        self.booking.click_on_i_agree()

    def SearchValue(self):
        self.search.set_type("Economy")
        self.search.set_trip_travel("one")
        self.search.set_flying_from("Lahore", "LHE")
        self.search.set_destination_to("Dubai", "DXB")
        self.search.set_depart_date("August 2023", "16")
        # self.search.set_travellers("adult", 1)
        self.search.click_search_button()
        time.sleep(2)
        self.search.click_select_flight()

    def test_BookWithValidInfoBySearch(self):
        self.prev_booking_number = self.booking.get_booking_number()
        self.booking.goto_flights()
        self.SearchValue()
        self.set_value()
        self.booking.click_on_confirm_booking()
        time.sleep(5)
        self.booking.go_to_dashboard()
        actual_result = self.booking.get_booking_number()
        time.sleep(5)
        expected_result = int(self.prev_booking_number) + 1
        baseSetUp.check_result_string(actual_result, str(expected_result))

    def test_FeaturedFlightBook(self):
        self.prev_booking_number = self.booking.get_booking_number()
        self.booking.goto_flights()
        self.booking.click_featured_flight(0)
        self.booking.click_on_select_flight(0)
        self.set_value()
        self.booking.click_on_confirm_booking()
        time.sleep(5)
        self.booking.go_to_dashboard()
        time.sleep(5)
        actual_result = self.booking.get_booking_number()
        expected_result = int(self.prev_booking_number) + 1
        baseSetUp.check_result_string(actual_result, str(expected_result))


def suit():
    test_suit = unittest.TestSuite()
    test_suit.addTest(FlightSearch("test_BookWithValidInfoBySearch"))
    test_suit.addTest(FlightSearch("test_FeaturedFlightBook"))

    return test_suit
