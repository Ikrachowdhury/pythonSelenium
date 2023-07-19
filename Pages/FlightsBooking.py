import time
from selenium.webdriver import Keys
from Base import Util


class BookFlight:
    def __init__(self, driver):
        self.Flight = None
        self.booking_number = None
        self.selector = None
        self.find = Util.ElementsUtil(driver)

    def goto_flights(self):
        self.Flight = self.find.element_by_xpath("//a[normalize-space()='Flights']")
        self.Flight.click()

    def select_dropdown(self, value, selector):
        # view_payment = self.find.element_by_xpath("//h3[normalize-space()='Payment Methods']")
        # self.find.scroll_to(view_payment)
        # time.sleep(5)
        self.selector = self.find.element_by_name(selector)
        self.find.scroll_to(self.selector)
        time.sleep(5)
        self.selector.click()
        self.find.dropdown(value, self.selector)
        time.sleep(2)

    def set_title(self, value):
        self.select_dropdown(value, "title_1")

    def set_first_name(self, value):
        first_name = self.find.element_by_name("first_name_1")
        first_name.click()
        first_name.send_keys(value)

    def set_last_name(self, value):
        last_namen = self.find.element_by_name("last_name_1")
        last_namen.click()
        last_namen.send_keys(value)

    def set_nationality_traveller(self, value):
        self.select_dropdown(value, "nationality_1")

    def set_birth_date_month(self, value):
        self.select_dropdown(value, "dob_month_1")

    def set_birth_date(self, value):
        self.select_dropdown(value, "dob_day_1")

    def set_birth_year(self, value):
        self.select_dropdown(value, "dob_year_1")

    def set_nid(self, value):
        nid = self.find.element_by_name("passport_1")
        nid.click()
        nid.send_keys(value)

    def set_issuance_day_month(self, value):
        self.select_dropdown(value, "passport_issuance_month_1")

    def set_issuance_day(self, value):
        self.select_dropdown(value, "passport_issuance_day_1")

    def set_issuance_year(self, value):
        self.select_dropdown(value, "passport_issuance_year_1")

    def set_expiry_day_month(self, value):
        self.select_dropdown(value, "passport_month_expiry_1")

    def set_expiry_day(self, value):
        self.select_dropdown(value, "passport_day_expiry_1")

    def set_set_expiry_year(self, value):
        self.select_dropdown(value, "passport_year_expiry_1")

    def set_payment_method(self, value):
        payment_name = None
        if value == "paypal":
            payment_name = "gateway_paypal"
        elif value == "bank":
            payment_name = "gateway_bank_transfer"
        elif value == "later":
            payment_name = "gateway_pay_later"
        elif value == "stripe":
            payment_name = "gateway_stripe"
        elif value == "wallet":
            payment_name = "gateway_wallet_balance"
        elif value == "duffle":
            payment_name = "gateway_duffel"
        payment = self.find.element_by_id(payment_name)
        self.find.scroll_to(payment)
        time.sleep(5)
        payment.click()

    def click_on_i_agree(self):
        agree_box = self.find.element_by_id("agreechb")
        self.find.scroll_to(agree_box)
        time.sleep(5)
        agree_box.click()

    def click_on_confirm_booking(self):
        confirm_button = self.find.element_by_id("booking")
        confirm_button.click()

    def go_to_dashboard(self):
        self.find.driver.get("https://phptravels.net/dashboard")

    def go_my_bookings(self, value):
        my_booking = self.find.element_by_xpath("(//a[normalize-space()='My Bookings'])[1]")
        my_booking.click()
        booking_id = self.find.element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[1]').text
        if value == booking_id:
            return booking_id
        else:
            return None

    def get_booking_number(self):
        self.booking_number = self.find.element_by_xpath("//div[3]//div[1]//h1[1]//strong[1]")
        return self.booking_number.text

    def click_featured_flight(self, value):

        feature_all = self.find.array_of_table("class", "col-lg-6")
        length = len(feature_all)
        for i in range(length):
            if i == value:
                element = feature_all[i]
                self.find.scroll_to(element)
                time.sleep(6)
                element.click()
                break

    def click_on_select_flight(self, value):
        flight_all = self.find.array_of_table("class", "mix")
        element = flight_all[value]
        time.sleep(5)
        self.find.scroll_to(element)
        time.sleep(5)
        flight = self.find.get_table_element(flight_all, value, "btn-dark")
        flight.click()
