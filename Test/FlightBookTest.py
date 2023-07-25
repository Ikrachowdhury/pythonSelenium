import time
import unittest
from Base import SetUp
from Test import SearchFlightTest
from Pages import FlightsBooking

baseSetUp = SetUp.MyTestCase()


class FlightSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        baseSetUp.setUp()
        baseSetUp.admin_login()

    def setUp(self):
        self.page_objects()

    def page_objects(self):
        self.search_flight = SearchFlightTest.FlightSearch()
        self.booking = FlightsBooking.BookFlight(baseSetUp.driver)

    def set_value(self):
        self.booking.set_title("Miss")
        self.booking.set_first_name("Ikra")
        self.booking.set_last_name("Chy")
        self.booking.set_nationality_traveller("Bangladesh")
        self.booking.set_nid("012345678901234")
        self.booking.set_payment_method("paypal")
        self.booking.click_on_i_agree()

    def test_BookWithValidInfoBySearch(self):
        self.prev_booking_number = self.booking.get_booking_number()
        self.search_flight.test_SearchFlightValid()
        self.set_value()
        self.booking.click_on_confirm_booking()
        time.sleep(5)
        actual_result = self.booking.get_booking_number()
        expected_result = int(self.prev_booking_number) + 1
        baseSetUp.check_result_string(actual_result, str(expected_result))
        # self.test_BookingCheck()

    def test_FeaturedFlightBook(self):
        self.prev_booking_number = self.booking.get_booking_number()
        self.booking.goto_flights()
        self.booking.click_featured_flight(0)
        self.booking.click_on_select_flight(0)
        self.set_value()
        self.booking.click_on_confirm_booking()
        time.sleep(10)
        self.booking.go_to_dashboard()
        actual_result = self.booking.get_booking_number()
        expected_result = int(self.prev_booking_number)+1
        baseSetUp.check_result_string(actual_result, str(expected_result))

    def test_BookingCheck(self):
        self.booking.go_to_dashboard()
        actual_result = self.booking.go_my_bookings("")
        baseSetUp.check_result_string(actual_result, "")
