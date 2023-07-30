from Test.FlightAirlineTest import suit as airline_suit
from Test.FlightAddtest import suit as add_flight_suit
from Test.FlightAirportTest import suit as airport_suit
from Test.FlightsAllTest import suit as flight_all_suit
from Test.FlightFeaturedTest import suit as featured_suit
from Test.FlightSuggestionTest import suit as suggestion_suit

import unittest
#
major_suits = unittest.TestSuite(
    [add_flight_suit(), airport_suit(), airline_suit(),featured_suit(), flight_all_suit(), suggestion_suit()])
# major_suits = unittest.TestSuite(
#     [flight_all_suit()])
unittest.TextTestRunner().run(major_suits)
