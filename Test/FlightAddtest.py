import time
import unittest
from Base import SetUp
from Pages import FlightsAll, DashBoard, FlightAirPort, FlightsAirline, FlightFeatured

baseSetUp = SetUp.MyTestCase()


class FlightValueAdd(unittest.TestCase):
    def setUp(self):
        baseSetUp.setUpClass()
        baseSetUp.setUp()
        self.page_objects()

    def page_objects(self):
        self.dashboard = DashBoard.DashBoard(SetUp.driver)
        self.flight = FlightsAll.FlightView(SetUp.driver)
        self.flightAirPortView = FlightAirPort.FlightAirPortView(SetUp.driver)
        self.flightAirlineView = FlightsAirline.FlightAirlineView(SetUp.driver)
        self.flightFeaturedView = FlightFeatured.FlightFeaturedView(SetUp.driver)

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
        self.flightFeaturedAdd = FlightFeatured.AddFlightFeatured(SetUp.driver)
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
        self.flightAdd.set_departure_time()
        self.flightAdd.set_arrival_time()
        self.flightAdd.set_baggage("5")
        self.flightAdd.set_cabin_baggage("3")

        self.flightAdd.set_adult_price("1000")
        self.flightAdd.set_child_price("500")
        self.flightAdd.set_infant_price("90")

    def flight_go(self):
        self.dashboard.goto_all_flights()
        time.sleep(5)
        self.dashboard.goto_all_flights()

    def test_add_airport(self):
        # self.test_ModuleStatus()
        self.dashboard.goto_Modules()
        self.dashboard.goto_all_flights()

        # Airports Adding
        self.dashboard.goto_airport_flight()
        self.flightAirPortView.click_Add_button()
        self.flightAirPortAdd = FlightAirPort.AddFlightAirPort(SetUp.driver)
        self.airport_value_1()
        self.flightAirPortAdd.click_on_save()
        time.sleep(3)
        self.flightAirPortView.click_Add_button()
        self.flightAirPortAdd = FlightAirPort.AddFlightAirPort(SetUp.driver)
        self.airport_value_2()
        self.flightAirPortAdd.click_on_save()
        time.sleep(3)

        # Airline Adding
        self.flight_go()
        self.dashboard.goto_airline_flight()
        self.flightAirlineView.click_Add_button()
        self.flightAirlineAdd = FlightsAirline.AddFlightAirline(SetUp.driver)
        self.airline_values()
        self.flightAirlineAdd.click_on_save()
        time.sleep(5)

        # Featured Flight
        self.flight_go()
        self.dashboard.goto_featured_flight()
        self.flightFeaturedView.click_Add_button()
        self.flightFeaturedAdd = FlightFeatured.AddFlightFeatured(SetUp.driver)
        self.featured_values()
        self.flightFeaturedAdd.click_on_save()
        time.sleep(3)

        self.flight_go()
        self.dashboard.goto_flights()
        self.flight.click_add_button()
        self.flightAdd = FlightsAll.FlightAdd(SetUp.driver)
        self.flight_values()
        self.flightAdd.click_on_save()
        time.sleep(3)


    @classmethod
    def tearDownClass(cls):
        SetUp.driver.close()

    if __name__ == '__main__':
        unittest.main()
