from Test.FlightAirlineTest import suit as airline_suit
from Test.FlightAddtest import suit as add_flight_suit
from Test.FlightAirportTest import suit as airport_suit
from Test.FlightsAllTest import suit as flight_all_suit
from Test.FlightFeaturedTest import suit as featured_suit
from Test.FlightSuggestionTest import suit as suggestion_suit
from Test.FlightBookTest import suit as flight_book_suit

import unittest

flight_suits = unittest.TestSuite(
    [airport_suit(), airline_suit(), featured_suit(), suggestion_suit(), flight_all_suit(), add_flight_suit()])
# major_suits = unittest.TestSuite(
#     [flight_all_suit()])
booking_suits = unittest.TestSuite([flight_book_suit()])
# unittest.TextTestRunner().run(flight_suits)
unittest.TextTestRunner().run(booking_suits)
