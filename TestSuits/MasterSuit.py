import unittest

from Test.FlightFeaturedTest import FlightFeaturedTesCases
from Test.FlightAirportTest import FlightAirportTesCases
from Test.FlightAirlineTest import FlightAirlineTesCases
from Test.FlightsAllTest import FlightsAllTesCases
from Test.FlightAddtest import FlightValueAdd

master_suit = unittest.TestSuite()
flight_add = unittest.TestLoader().loadTestsFromTestCase(FlightValueAdd)
flight_featured = unittest.TestLoader().loadTestsFromTestCase(FlightFeaturedTesCases)
flight_airport = unittest.TestLoader().loadTestsFromTestCase(FlightAirportTesCases)
flight_airline = unittest.TestLoader().loadTestsFromTestCase(FlightAirlineTesCases)
flight_all = unittest.TestLoader().loadTestsFromTestCase(FlightsAllTesCases)

unittest.TextTestRunner().run(master_suit)
