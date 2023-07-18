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
    def test_FightAirportPageAppear(self):
        self.dashboard.goto_all_flights()
        self.dashboard.goto_airport_flight()
        time.sleep(3)
        pageTittle = SetUp.driver.title
        # print(pageTittle)
        baseSetUp.check_result_string(pageTittle, "Airports")

    def test_AddNewAirportPageAppear(self):
        self.test_FightAirportPageAppear()
        pageStart = self.flightAirPortView.click_Add_button()
        baseSetUp.check_result_string(pageStart, "Status")

    def test_EditButton(self):
        pass

    def test_DeleteButton(self):
        self.test_FightAirportPageAppear()
        self.flightAirPortView.click_delete_button(0,"yes")
        time.sleep(3)

    def test_StatusChange(self):
        self.test_FightAirportPageAppear()
        self.flightAirPortView.click_satus(0)
        time.sleep(2)
        actualResult = self.flightAirPortView.get_text_popup()
        baseSetUp.check_result_string(actualResult,
                                      "Info Updated\n" + "Information updated successfully")
        time.sleep(6)

    def test_ClickCheckbox(self):
        self.test_FightAirportPageAppear()
        actualResult = self.flightAirPortView.click_checkbox(0)
        baseSetUp.check_result_string(actualResult, "deleteAll")
        time.sleep(3)

    def test_DeleteAll(self):
        self.test_ClickCheckbox()
        self.flightAirPortView.click_checkbox_all()

    # **************************************************Flight search section Test Cases*************************
    def test_ClickSearchAirportAppear(self):
        self.test_FightAirportPageAppear()
        actualResult = self.flightAirPortView.click_search_button()
        baseSetUp.check_result_string(actualResult, "Go")
        time.sleep(3)

    def test_SearchAirportValid(self):
        self.test_ClickSearchAirportAppear()
        self.flightAirPortView.set_field_dropbox("All fields")
        self.flightAirPortView.set_no_dropBox("1")
        self.flightAirPortView.set_input_box("Al Masna'ah")
        actualResult = self.flightAirPortView.click_on_go()
        baseSetUp.check_result_string(actualResult, "Reset")
        time.sleep(6)

    def test_Reset_button(self):
        self.test_ClickSearchAirportAppear()
        time.sleep(3)
        actualResult = self.flightAirPortView.click_on_reset()
        baseSetUp.check_result_string(actualResult, "mainpage")
        time.sleep(3)

    # *********************************************************** Add Airport Test Cases ***************************

    def AirportValues(self):
        self.test_AddNewAirportPageAppear()
        self.flightAirPortAdd = FlightAirPort.AddFlightAirPort(SetUp.driver)
        self.flightAirPortAdd.set_status("Enabled")
        # self.flightAirPortAdd.set_code("CTG_1")
        # self.flightAirPortAdd.set_airport("Ctg Airport")
        # self.flightAirPortAdd.set_city("Chattogram")
        self.flightAirPortAdd.set_country("Bangladesh")
        #
        self.flightAirPortAdd.set_code("DHK-1")
        self.flightAirPortAdd.set_airport("Dhaka Airport")
        self.flightAirPortAdd.set_city("Dhaka")

    def test_AddANewAirportValid(self):
        self.AirportValues()
        self.flightAirPortAdd.click_on_save()
        # actualResult = self.flightAirPortView.get_first_element_from_table()
        # print(actualResult)
        # expectedResult = ('CTG_1', 'Ctg Airport', 'Chattogram')
        # baseSetUp.check_result_string(actualResult,expectedResult)
        time.sleep(4)

    def test_AddWithoutValue(self):
        self.test_AddNewAirportPageAppear()
        self.flightAirPortAdd = FlightAirPort.AddFlightAirPort(SetUp.driver)
        self.flightAirPortAdd.set_status("")
        self.flightAirPortAdd.set_code("")
        self.flightAirPortAdd.set_airport("")
        self.flightAirPortAdd.set_city("")
        self.flightAirPortAdd.set_country("")
        self.flightAirPortAdd.click_on_save()

    def test_AddSameAirportTwice(self):
        self.AirportValues()
        self.flightAirPortAdd.click_on_save()

        actualResult = self.flightAirPortAdd.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Flight Already exits")
        time.sleep(3)

    def test_AddAirportInvalid(self):
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
