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

    def test_BookWithValidInfo(self):
        self.search_flight.test_SearchFlightValid()
        self.booking.set_title("Miss")
        self.booking.set_first_name("Ikra")
        self.booking.set_last_name("Chy")
        self.booking.set_nationality_traveller("Bangladesh")
        self.booking.set_nid("012345678901234")
        time.sleep(5)
