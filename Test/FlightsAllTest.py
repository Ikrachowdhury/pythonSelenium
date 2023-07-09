import time
import unittest
from Base import SetUp
from Pages import FlightsAll, DashBoard

baseSetUp = SetUp.MyTestCase()


class FlightsAllTesCases(unittest.TestCase):

    def setUp(self):
        baseSetUp.setUpClass()
        baseSetUp.setUp()
        self.page_objects()

    def page_objects(self):
        self.dashboard = DashBoard.DashBoard(SetUp.driver)
        self.flight = FlightsAll.FlightView(SetUp.driver)
        self.flightAdd = None







    # *************************************View Section test Cases***********************************************************************************
    def test_flightPageAppear_TC1(self):
        self.dashboard.goto_all_flights()
        self.dashboard.goto_flights()
        pageTittle = SetUp.driver.title
        # print(pageTittle)
        baseSetUp.check_result_string(pageTittle, "Flights")

    def test_AddNewFlightOptionAppear_TC2(self):
        self.test_flightPageAppear_TC1()
        self.flight.click_add_button()
        time.sleep(6)
        pageStart = self.flight.get_AddFlight_identifier()
        # print(pageStart)
        baseSetUp.check_result_string(pageStart, "Status")

    def test_EditButton_TC14(self):
        self.test_flightPageAppear_TC1()
        self.flight.click_edit_button(0)
        time.sleep(6)
        pageStart = self.flight.get_EditFlight_identifier()
        print(pageStart)
        baseSetUp.check_result_string(pageStart, "Status")

    def test_DeleteButton_TC10(self):
        self.test_flightPageAppear_TC1()
        self.flight.click_delete_button(0)
        time.sleep(6)

    def test_StatusChange_TC8(self):
        self.test_flightPageAppear_TC1()
        self.flight.click_satus(0)
        time.sleep(2)
        actualResult = self.flight.get_text_popup()
        baseSetUp.check_result_string(actualResult,
                                      "Info Updated\n" + "Information updated successfully")
        time.sleep(6)

    def test_ClickCheckbox_TC9(self):
        self.test_flightPageAppear_TC1()
        actualResult = self.flight.click_checkbox(0)
        baseSetUp.check_result_string(actualResult, "deleteAll")
        time.sleep(3)

    def test_DeleteAll_TC15(self):
        self.test_ClickCheckbox_TC9()
        self.flight.click_delete_all()

    #**************************************************Flight search section Test Cases*************************
    def test_ClickSearchFlightBoxAppear_TC16n17(self):
        self.test_flightPageAppear_TC1()
        actualResult = self.flight.click_search_button()
        baseSetUp.check_result_string(actualResult, "Go")
        time.sleep(3)

    def test_SearchFlightValid_TC16(self):
        self.test_ClickSearchFlightBoxAppear_TC16n17()
        self.flight.set_field_dropdown("User_id")
        time.sleep(2)
        self.flight.set_type_box("economy")
        time.sleep(2)
        self.flight.set_no_drop_box("0")
        time.sleep(2)
        self.flight.set_input_box("Demo Supplier")
        time.sleep(2)
        actualResult = self.flight.click_on_go()
        baseSetUp.check_result_string(actualResult, "Reset")
        time.sleep(6)

    def test_SearchFlightInvalid_TC17(self):
        self.test_ClickSearchFlightBoxAppear_TC16n17()
        self.flight.set_field_dropdown("User_id")
        time.sleep(2)
        self.flight.set_type_box("local")
        time.sleep(2)
        self.flight.set_no_drop_box("9")
        time.sleep(2)
        self.flight.set_input_box("fdsjhffk")
        time.sleep(2)
        actualResult = self.flight.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Invalid input")
        time.sleep(6)
     #************************************************************ search end****************************************
    def test_Back_button(self):
        self.test_flightPageAppear_TC1()
        actualResult = self.flight.click_back_button()
        baseSetUp.check_result_string(actualResult, "Dashboard")
        time.sleep(3)
    #*******************************************************************************************************************************************************






    #*********************************************************** Add Flights Test Cases *******************************************************************
    def test_AddANewFlightValid_TC2(self):
        self.test_AddNewFlightOptionAppear_TC2()
        self.flightAdd = FlightsAll.FlightAdd(SetUp.driver)
        self.flightAdd.set_id("")
        self.flightAdd.select_option("")
        self.flightAdd.set_type("")
        self.flightAdd.set_airline("")
        self.flightAdd.set_baggage("")
        self.flightAdd.set_duration("")
        self.flightAdd.set_airport_from("")
        self.flightAdd.set_airport_to("")
        self.flightAdd.set_departure_time("")
        self.flightAdd.set_refundable("")
        self.flightAdd.set_adult_price("")
        self.flightAdd.set_infant_price("")
        self.flightAdd.set_child_price("")
        self.flightAdd.set_status("")
        self.flightAdd.set_arrival_time("")

    def test_AddWithoutValue_TC2(self):
        self.test_AddNewFlightOptionAppear_TC2()
        self.flightAdd = FlightsAll.FlightAdd(SetUp.driver)
        self.flightAdd.set_id("")
        self.flightAdd.select_option("")
        self.flightAdd.set_type("")
        self.flightAdd.set_airline("")
        self.flightAdd.set_baggage("")
        self.flightAdd.set_duration("")
        self.flightAdd.set_airport_from("")
        self.flightAdd.set_airport_to("")
        self.flightAdd.set_departure_time("")
        self.flightAdd.set_refundable("")
        self.flightAdd.set_adult_price("")
        self.flightAdd.set_infant_price("")
        self.flightAdd.set_child_price("")
        self.flightAdd.set_status("")
        self.flightAdd.set_arrival_time("")
        self.flightAdd.Save()

    def test_AddSameFlightTwice_TC4(self):
        self.test_AddNewFlightOptionAppear_TC2()
        self.flightAdd = FlightsAll.FlightAdd(SetUp.driver)
        self.flightAdd.set_id("")
        self.flightAdd.select_option("")
        self.flightAdd.set_type("")
        self.flightAdd.set_airline("")
        self.flightAdd.set_baggage("")
        self.flightAdd.set_duration("")
        self.flightAdd.set_airport_from("")
        self.flightAdd.set_airport_to("")
        self.flightAdd.set_departure_time("")
        self.flightAdd.set_refundable("")
        self.flightAdd.set_adult_price("")
        self.flightAdd.set_infant_price("")
        self.flightAdd.set_child_price("")
        self.flightAdd.set_status("")
        self.flightAdd.set_arrival_time("")
        self.flightAdd.Save()

    def test_AddFlightWrongInfo_TC5(self):
        self.test_AddNewFlightOptionAppear_TC2()
        self.flightAdd = FlightsAll.FlightAdd(SetUp.driver)
        self.flightAdd.set_id("")
        self.flightAdd.select_option("")
        self.flightAdd.set_type("")
        self.flightAdd.set_airline("")
        self.flightAdd.set_baggage("")
        self.flightAdd.set_duration("")
        self.flightAdd.set_airport_from("")
        self.flightAdd.set_airport_to("")
        self.flightAdd.set_departure_time("")
        self.flightAdd.set_refundable("")
        self.flightAdd.set_adult_price("")
        self.flightAdd.set_infant_price("")
        self.flightAdd.set_child_price("")
        self.flightAdd.set_status("")
        self.flightAdd.set_arrival_time("")
        self.flightAdd.Save()

    def test_AddSameFlight_PriceInput_TC6(self):
        self.test_AddNewFlightOptionAppear_TC2()
        self.flightAdd = FlightsAll.FlightAdd(SetUp.driver)
        self.flightAdd.set_id("")
        self.flightAdd.select_option("")
        self.flightAdd.set_type("")
        self.flightAdd.set_airline("")
        self.flightAdd.set_baggage("")
        self.flightAdd.set_duration("")
        self.flightAdd.set_airport_from("")
        self.flightAdd.set_airport_to("")
        self.flightAdd.set_departure_time("")
        self.flightAdd.set_refundable("")
        self.flightAdd.set_adult_price("")
        self.flightAdd.set_infant_price("")
        self.flightAdd.set_child_price("")
        self.flightAdd.set_status("")
        self.flightAdd.set_arrival_time("")
        self.flightAdd.Save()
    def test_AddSameFlight_TimeInput_TC7(self):
        self.test_AddNewFlightOptionAppear_TC2()
        self.flightAdd = FlightsAll.FlightAdd(SetUp.driver)
        self.flightAdd.set_id("")
        self.flightAdd.select_option("")
        self.flightAdd.set_type("")
        self.flightAdd.set_airline("")
        self.flightAdd.set_baggage("")
        self.flightAdd.set_duration("")
        self.flightAdd.set_airport_from("")
        self.flightAdd.set_airport_to("")
        self.flightAdd.set_departure_time("")
        self.flightAdd.set_refundable("")
        self.flightAdd.set_adult_price("")
        self.flightAdd.set_infant_price("")
        self.flightAdd.set_child_price("")
        self.flightAdd.set_status("")
        self.flightAdd.set_arrival_time("")
        self.flightAdd.Save()

    @classmethod
    def tearDownClass(cls):
        SetUp.driver.close()

    if __name__ == '__main__':
        unittest.main()
