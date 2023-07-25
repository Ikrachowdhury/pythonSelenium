import unittest

from Test.FlightFeaturedTest import FlightFeaturedTesCases
from Test.FlightAirportTest import FlightAirportTesCases
from Test.FlightAirlineTest import FlightAirlineTesCases
from Test.FlightsAllTest import FlightsAllTesCases

flight_add_suit = unittest.TestSuite()


flight_add_suit.addTest(FlightAirportTesCases("test_AddANewAirportValid_1"))
flight_add_suit.addTest(FlightAirportTesCases("test_AddANewAirportValid_2"))
flight_add_suit.addTest(FlightAirlineTesCases("test_AddANewAirlineValid"))
flight_add_suit.addTest(FlightsAllTesCases("test_AddANewFlightValid_TC2"))
flight_add_suit.addTest(FlightFeaturedTesCases("test_AddANewFeaturedValid"))

unittest.TextTestRunner().run(flight_add_suit)
