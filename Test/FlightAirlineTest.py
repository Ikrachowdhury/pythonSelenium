import time
import unittest
from Base import SetUp
from Pages import FlightsAirline, DashBoard

baseSetUp = SetUp.MyTestCase()


class FlightAirlineTesCases(unittest.TestCase):

    def setUp(self):
        baseSetUp.setUpClass()
        baseSetUp.setUp()
        self.page_objects()

    def page_objects(self):
        self.dashboard = DashBoard.DashBoard(SetUp.driver)
        self.flightAirlineView = FlightsAirline.FlightAirlineView(SetUp.driver)
        self.flightAirlineAdd = None

    # *************************************View Section test Cases***********************************************************************************
    def test_FightAirlinePageAppear_TC(self):
        self.dashboard.goto_all_flights()
        self.dashboard.goto_airline_flight()
        time.sleep(3)
        pageTittle = SetUp.driver.title
        # print(pageTittle)
        baseSetUp.check_result_string(pageTittle, "Airlines")

    def test_AddNewAirlinePageAppear_TC2(self):
        self.test_FightAirlinePageAppear_TC()
        pageStart = self.flightAirlineView.click_Add_button()
        baseSetUp.check_result_string(pageStart, "Status")

    def test_EditButton_TC14(self):
        pass

    def test_DeleteButton_TC10(self):
        pass

    def test_StatusChange_TC8(self):
        self.test_FightAirlinePageAppear_TC()
        self.flightAirlineView.click_satus(0)
        time.sleep(2)
        actualResult = self.flightAirlineView.get_text_popup()
        baseSetUp.check_result_string(actualResult,
                                      "Info Updated\n" + "Information updated successfully")
        time.sleep(6)

    def test_ClickCheckbox_TC9(self):
        self.test_FightAirlinePageAppear_TC()
        actualResult = self.flightAirlineView.click_checkbox(0)
        baseSetUp.check_result_string(actualResult, "deleteAll")
        time.sleep(3)

    def test_DeleteAll_TC15(self):#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.test_ClickCheckbox_TC9()
        self.flightAirlineView.click_checkbox_all()

    # **************************************************Flight search section Test Cases*************************
    def test_ClickSearchAirlineAppear_TC16n17(self):
        self.test_FightAirlinePageAppear_TC()
        actualResult = self.flightAirlineView.click_search_button()
        baseSetUp.check_result_string(actualResult, "Go")
        time.sleep(3)

    def test_SearchAirlineValid_TC16(self):
        self.test_ClickSearchAirlineAppear_TC16n17()
        self.flightAirlineView.set_field_dropbox("All fields")
        self.flightAirlineView.set_no_dropBox("1")
        self.flightAirlineView.set_input_box("Russia")
        actualResult = self.flightAirlineView.click_on_go()
        baseSetUp.check_result_string(actualResult, "Reset")
        time.sleep(6)

    def test_Reset_button(self):
        self.test_ClickSearchAirlineAppear_TC16n17()
        time.sleep(3)
        actualResult = self.flightAirlineView.click_on_reset()
        baseSetUp.check_result_string(actualResult, "mainpage")
        time.sleep(3)

    # ************************************************************ search end****************************************

    # *******************************************************************************************************************************************************

    # *********************************************************** Add Airport Test Cases ***************************

    def AirlineValues(self):#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.test_AddNewAirlinePageAppear_TC2()
        self.flightAirlineAdd = FlightsAirline.AddFlightAirline(SetUp.driver)
        self.flightAirlineAdd.set_status("Enabled")
        self.flightAirlineAdd.set_iata("BNG")
        self.flightAirlineAdd.set_name("Bangladesh Airline")
        self.flightAirlineAdd.set_country("Bangladesh")

    def test_AddANewAirlineValid_TC2(self):#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.AirlineValues()
        self.flightAirlineAdd.click_on_save()
        time.sleep(4)

    def test_AddWithoutValue_TC2(self):#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.test_AddNewAirlinePageAppear_TC2()
        self.flightAirlineAdd = FlightsAirline.AddFlightAirline(SetUp.driver)
        self.flightAirlineAdd.set_status("")
        self.flightAirlineAdd.set_status("")
        self.flightAirlineAdd.set_iata("")
        self.flightAirlineAdd.set_name("")
        self.flightAirlineAdd.set_country("")
        self.flightAirlineAdd.click_on_save()

    def test_AddSameAirlineTwice_TC4(self):
        self.AirlineValues()
        self.flightAirlineAdd.click_on_save()

        actualResult = self.flightAirlineAdd.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Flight Already exits")
        time.sleep(3)

    def test_AddAirlineInvalid_TC5(self):
        self.AirlineValues()
        self.flightAirlineAdd.set_airport("kjwhiu")
        self.flightAirlineAdd.set_city("123")
        self.flightAirlineAdd.click_on_save()

        actualResult = self.flightAirlineAdd.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Invalid input")
        time.sleep(3)



    @classmethod
    def tearDownClass(cls):
        SetUp.driver.close()

    if __name__ == '__main__':
        unittest.main()