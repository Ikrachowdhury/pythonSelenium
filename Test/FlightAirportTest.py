import time
import unittest
from Base import SetUp
from Pages import FlightAirPort, DashBoard

baseSetUp = SetUp.MyTestCase()


class FlightAirportTesCases(unittest.TestCase):

    def setUp(self):
        baseSetUp.setUpClass()
        baseSetUp.setUp()
        self.page_objects()

    def page_objects(self):
        self.dashboard = DashBoard.DashBoard(SetUp.driver)
        self.flightAirPortView = FlightAirPort.FlightAirPortView(SetUp.driver)
        self.flightAirPortAdd = None  # FlightAirPort.FlightAirPortView(SetUp.driver)

    # *************************************View Section test Cases***********************************************************************************
    def test_FightAirportPageAppear_TC(self):
        self.dashboard.goto_all_flights()
        self.dashboard.goto_airport_flight()
        time.sleep(3)
        pageTittle = SetUp.driver.title
        # print(pageTittle)
        baseSetUp.check_result_string(pageTittle, "Airports")

    def test_AddNewAirportPageAppear_TC2(self):
        self.test_FightAirportPageAppear_TC()
        pageStart = self.flightAirPortView.click_Add_button()
        baseSetUp.check_result_string(pageStart, "Status")

    def test_EditButton_TC14(self):
        pass

    def test_DeleteButton_TC10(self):
        pass

    def test_StatusChange_TC8(self):
        self.test_FightAirportPageAppear_TC()
        self.flightAirPortView.click_satus(0)
        time.sleep(2)
        actualResult = self.flightAirPortView.get_text_popup()
        baseSetUp.check_result_string(actualResult,
                                      "Info Updated\n" + "Information updated successfully")
        time.sleep(6)

    def test_ClickCheckbox_TC9(self):
        self.test_FightAirportPageAppear_TC()
        actualResult = self.flightAirPortView.click_checkbox(0)
        baseSetUp.check_result_string(actualResult, "deleteAll")
        time.sleep(3)

    def test_DeleteAll_TC15(self):
        self.test_ClickCheckbox_TC9()
        self.flightAirPortView.click_checkbox_all()

    # **************************************************Flight search section Test Cases*************************
    def test_ClickSearchAirportAppear_TC16n17(self):
        self.test_FightAirportPageAppear_TC()
        actualResult = self.flightAirPortView.click_search_button()
        baseSetUp.check_result_string(actualResult, "Go")
        time.sleep(3)

    def test_SearchAirportValid_TC16(self):
        self.test_ClickSearchAirportAppear_TC16n17()
        self.flightAirPortView.set_field_dropbox("All fields")
        self.flightAirPortView.set_no_dropBox("1")
        self.flightAirPortView.set_input_box("Al Masna'ah")
        actualResult = self.flightAirPortView.click_on_go()
        baseSetUp.check_result_string(actualResult, "Reset")
        time.sleep(6)

    def test_Reset_button(self):
        self.test_ClickSearchAirportAppear_TC16n17()
        time.sleep(3)
        actualResult = self.flightAirPortView.click_on_reset()
        baseSetUp.check_result_string(actualResult, "mainpage")
        time.sleep(3)

    # ************************************************************ search end****************************************

    # *******************************************************************************************************************************************************

    # *********************************************************** Add Airport Test Cases ***************************

    def AirportValues(self):#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.test_AddNewAirportPageAppear_TC2()
        self.flightAirPortAdd = FlightAirPort.AddFlightAirPort(SetUp.driver)
        self.flightAirPortAdd.set_status("Enabled")
        self.flightAirPortAdd.set_code("NS0")
        self.flightAirPortAdd.set_airport("Dhaka Airport")
        self.flightAirPortAdd.set_city("Dhaka")
        self.flightAirPortAdd.set_country("Bangladesh")

    def test_AddANewAirportValid_TC2(self):#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.AirportValues()
        self.flightAirPortAdd.click_on_save()
        time.sleep(4)

    def test_AddWithoutValue_TC2(self):#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.test_AddNewAirportPageAppear_TC2()
        self.flightAirPortAdd = FlightAirPort.AddFlightAirPort(SetUp.driver)
        self.flightAirPortAdd.set_status("")
        self.flightAirPortAdd.set_code("")
        self.flightAirPortAdd.set_airport("")
        self.flightAirPortAdd.set_city("")
        self.flightAirPortAdd.set_country("")
        self.flightAirPortAdd.click_on_save()

    def test_AddSameAirportTwice_TC4(self):
        self.AirportValues()
        self.flightAirPortAdd.click_on_save()

        actualResult = self.flightAirPortAdd.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Flight Already exits")
        time.sleep(3)

    def test_AddAirportInvalid_TC5(self):
        self.AirportValues()
        self.flightAirPortAdd.set_airport("kjwhiu")
        self.flightAirPortAdd.set_city("123")
        self.flightAirPortAdd.click_on_save()

        actualResult = self.flightAirPortAdd.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Invalid input")
        time.sleep(3)



    @classmethod
    def tearDownClass(cls):
        SetUp.driver.close()

    if __name__ == '__main__':
        unittest.main()