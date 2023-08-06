import time
import unittest
from Base import SetUp
from Pages import FlightsAll, DashBoard, FlightAirPort, FlightsAirline, FlightFeatured, FlightSuggestion

baseSetUp = SetUp.MyTestCase()


class FlightValueAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        baseSetUp.setUp()
        baseSetUp.admin_login()

    def setUp(self):
        self.page_objects()

    def page_objects(self):
        self.dashboard = DashBoard.DashBoard(baseSetUp.driver)
        self.flight = FlightsAll.FlightView(baseSetUp.driver)
        self.flightAirPortView = FlightAirPort.FlightAirPortView(baseSetUp.driver)
        self.flightAirlineView = FlightsAirline.FlightAirlineView(baseSetUp.driver)
        self.flightFeaturedView = FlightFeatured.FlightFeaturedView(baseSetUp.driver)
        self.FlightSuggestionView = FlightSuggestion.FlightSuggestionView(baseSetUp.driver)

    def test_ModuleStatus(self):
        self.dashboard.goto_Modules()
        self.flightAirPortView.click_module_flight_status()
        time.sleep(2)

    def airport_value_1(self):
        self.flightAirPortAdd.set_status("Enabled")
        self.flightAirPortAdd.set_code("CTG_1")
        self.flightAirPortAdd.set_airport("Ctg Airport")
        self.flightAirPortAdd.set_city("Chattogram")
        self.flightAirPortAdd.set_country("Bangladesh")

    def airport_value_2(self):
        self.flightAirPortAdd.set_status("Enabled")
        self.flightAirPortAdd.set_code("DHK-1")
        self.flightAirPortAdd.set_airport("Dhaka Airport")
        self.flightAirPortAdd.set_city("Dhaka")
        self.flightAirPortAdd.set_country("Bangladesh")

    def airline_values(self):
        self.flightAirlineAdd.set_status("Enabled")
        self.flightAirlineAdd.set_iata("BNA")
        self.flightAirlineAdd.set_name("Air Bangladesh")
        self.flightAirlineAdd.set_country("Bangladesh")

    def featured_values(self):
        self.flightFeaturedAdd = FlightFeatured.AddFlightFeatured(baseSetUp.driver)
        self.flightFeaturedAdd.set_status("Enabled")
        self.flightFeaturedAdd.set_airline("135 Airways")
        self.flightFeaturedAdd.set_from_airport("CTG_1")
        self.flightFeaturedAdd.set_to_airport("DHK-1")
        self.flightFeaturedAdd.set_price("3000")

    def flight_values(self):
        self.flightAdd.set_status("Enabled")
        self.flightAdd.set_airline("Air Bangladesh")
        self.flightAdd.set_id("supplier@phptravels.com")
        self.flightAdd.set_airport_from("CTG_1")
        self.flightAdd.set_airport_to("DHK-1")
        self.flightAdd.set_duration("3H")
        self.flightAdd.set_type("Economy")
        self.flightAdd.set_refundable("Disable")
        # self.flightAdd.set_depart_date("August 2023", "16")
        # self.flightAdd.set_arrive_date("September 2023", "16")
        self.flightAdd.set_baggage("5")
        self.flightAdd.set_cabin_baggage("3")

        self.flightAdd.set_adult_price("1000")
        self.flightAdd.set_child_price("500")
        self.flightAdd.set_infant_price("90")

    def suggestion_values(self):
        self.FlightSuggestionAdd.set_status("Enabled")
        self.FlightSuggestionAdd.set_type("From_destination")
        self.FlightSuggestionAdd.set_city_airport("CTG_1")
        self.FlightSuggestionAdd.set_order("0")

    def flight_go(self):
        self.dashboard.goto_all_flights()
        time.sleep(5)
        self.dashboard.goto_all_flights()

    def test_add_airport(self):
        self.test_ModuleStatus()
        # self.dashboard.goto_Modules()
        self.dashboard.goto_all_flights()

        # Airports Adding
        self.dashboard.goto_airport_flight()
        self.flightAirPortView.click_Add_button()
        self.flightAirPortAdd = FlightAirPort.AddFlightAirPort(baseSetUp.driver)
        self.airport_value_1()
        self.flightAirPortAdd.click_on_save()
        time.sleep(3)
        self.flightAirPortView.click_Add_button()
        self.flightAirPortAdd = FlightAirPort.AddFlightAirPort(baseSetUp.driver)
        self.airport_value_2()
        self.flightAirPortAdd.click_on_save()
        time.sleep(3)

        # Airline Adding
        self.flight_go()
        self.dashboard.goto_airline_flight()
        self.flightAirlineView.click_Add_button()
        self.flightAirlineAdd = FlightsAirline.AddFlightAirline(baseSetUp.driver)
        self.airline_values()
        self.flightAirlineAdd.click_on_save()
        time.sleep(5)

        # Featured Flight
        self.flight_go()
        self.dashboard.goto_featured_flight()
        self.flightFeaturedView.click_Add_button()
        self.flightFeaturedAdd = FlightFeatured.AddFlightFeatured(baseSetUp.driver)
        self.featured_values()
        self.flightFeaturedAdd.click_on_save()
        time.sleep(3)

        self.flight_go()
        self.dashboard.goto_flights()
        self.flight.click_add_button()
        self.flightAdd = FlightsAll.FlightAdd(baseSetUp.driver)
        self.flight_values()
        self.flightAdd.click_on_save()
        time.sleep(3)

        self.flight_go()
        self.dashboard.goto_suggestion_flight()
        self.FlightSuggestionView.click_Add_button()
        self.FlightSuggestionAdd = FlightSuggestion.AddFlightSuggestion(baseSetUp.driver)
        self.suggestion_values()
        self.FlightSuggestionAdd.click_on_save()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        baseSetUp.driver.close()

    if __name__ == '__main__':
        unittest.main()


def suit():
    test_suit = unittest.TestSuite()
    test_suit.addTest(FlightValueAdd("test_add_airport"))
    return test_suit
