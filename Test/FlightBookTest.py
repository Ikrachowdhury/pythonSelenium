import time
import unittest
from Base import SetUp
from Test import SearchFlightTest
from Pages import FlightsBooking

baseSetUp = SetUp.MyTestCase()


class FlightSearch(unittest.TestCase):
    def setUp(self):
        baseSetUp.setUpClass()
        baseSetUp.agent_login()
        self.page_objects()

    def page_objects(self):
        self.search_flight = SearchFlightTest.FlightSearch()
        self.booking = FlightsBooking.BookFlight(SetUp.driver)

    def set_value(self):
        self.booking.set_title("Miss")
        self.booking.set_first_name("Ikra")
        self.booking.set_last_name("Chy")
        self.booking.set_nationality_traveller("Bangladesh")
        self.booking.set_nid("012345678901234")

    def test_BookWithValidInfo(self):
        self.search_flight.test_SearchFlightValid()
        self.set_value()
        self.booking.click_on_confirm_booking()
        time.sleep(5)
        self.test_BookingCheck()

    def test_FeaturedFlight(self):
        self.prev_booking_number = self.booking.get_booking_number()
        self.booking.goto_flights()
        self.booking.click_featured_flight(1)
        self.set_value()
        self.booking.click_on_confirm_booking()
        self.booking.go_to_dashboard()
        actual_result = self.booking.get_booking_number()
        baseSetUp.check_result_string(actual_result, self.prev_booking_number + 1)

    def test_BookingCheck(self):
        self.booking.go_to_dashboard()
        actual_result = self.booking.go_my_bookings("")
        baseSetUp.check_result_string(actual_result, "")
