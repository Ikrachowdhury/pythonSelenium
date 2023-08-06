from Base import Util
#dropdown error
class DashBoard:
    def __init__(self, driver):
        self.BookingFlight = None
        self.FlightSuggestion = None
        self.FlightFeatured = None
        self.FlightAirline = None
        self.FlightAirport = None
        self.Flight = None
        self.find = Util.ElementsUtil(driver)
        self.Modules = self.find.element_by_xpath('/html/body/main/header/ul/li[3]/a')
        self.Flights = None
        self.Booking = self.find.element_by_xpath("//a[normalize-space()='Bookings']")

    def goto_Modules(self):
        self.Modules.click()

    def goto_all_flights(self):
        self.Flights = self.find.element_by_xpath("//button[normalize-space()='Flights']")
        self.Flights.click()
        if self.Flights.is_displayed():
            self.Flight = self.find.element_by_xpath('//*[@id="flights-collapse"]/ul/li[1]/a')
            self.FlightAirport = self.find.element_by_xpath('//*[@id="flights-collapse"]/ul/li[2]/a')
            self.FlightAirline = self.find.element_by_xpath('//*[@id="flights-collapse"]/ul/li[3]/a')
            self.FlightFeatured = self.find.element_by_xpath('//*[@id="flights-collapse"]/ul/li[4]/a')
            self.FlightSuggestion = self.find.element_by_xpath('//*[@id="flights-collapse"]/ul/li[5]/a')
            return "ok"
        else:
            return "no"

    def goto_flights(self):
        self.Flight.click()

    def goto_airport_flight(self):
        self.FlightAirport.click()

    def goto_airline_flight(self):
        self.FlightAirline.click()

    def goto_featured_flight(self):
        self.FlightFeatured.click()

    def goto_suggestion_flight(self):
        self.FlightSuggestion.click()

    def goto_modules(self):
        self.Booking.click()
        self.BookingFlight = self.find.element_by_link("./flights_suggestions.php")

    def goto_booking_Flight(self):
        self.BookingFlight.click()
