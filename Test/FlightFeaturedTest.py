import time
import unittest
from Base import SetUp
from Pages import FlightFeatured, DashBoard

baseSetUp = SetUp.MyTestCase()


class FlightFeaturedTesCases(unittest.TestCase):

    def setUp(self):
        baseSetUp.setUpClass()
        baseSetUp.setUp()
        self.page_objects()

    def page_objects(self):
        self.dashboard = DashBoard.DashBoard(SetUp.driver)
        self.flightFeaturedView = FlightFeatured.FlightFeaturedView(SetUp.driver)
        self.flightFeaturedAdd = None  # FlightAirPort.FlightAirPortView(SetUp.driver)

    # *************************************View Section test Cases***********************************************************************************
    def test_FightFeaturedPageAppear_TC(self):
        self.dashboard.goto_all_flights()
        self.dashboard.goto_featured_flight()
        time.sleep(3)
        pageTittle = SetUp.driver.title
        # print(pageTittle)
        baseSetUp.check_result_string(pageTittle, "Flights Featured")

    def test_AddNewFeaturedPageAppear_TC2(self):
        self.test_FightFeaturedPageAppear_TC()
        pageStart = self.flightFeaturedView.click_Add_button()
        baseSetUp.check_result_string(pageStart, "Status")

    def test_EditButton_TC14(self):
        pass

    def test_DeleteButton_TC10(self):
        pass

    def test_StatusChange_TC8(self):
        self.test_FightFeaturedPageAppear_TC()
        self.flightFeaturedView.click_satus(0)
        time.sleep(2)
        actualResult = self.flightFeaturedView.get_text_popup()
        baseSetUp.check_result_string(actualResult,
                                      "Info Updated\n" + "Information updated successfully")
        time.sleep(6)

    def test_ClickCheckbox_TC9(self):
        self.test_FightFeaturedPageAppear_TC()
        actualResult = self.flightFeaturedView.click_checkbox(0)
        baseSetUp.check_result_string(actualResult, "deleteAll")
        time.sleep(3)

    def test_DeleteAll_TC15(self):
        self.test_ClickCheckbox_TC9()
        self.flightFeaturedView.click_checkbox_all()

    # **************************************************Flight search section Test Cases*************************
    def test_ClickSearchFeaturedAppear_TC16n17(self):
        self.test_FightFeaturedPageAppear_TC()
        actualResult = self.flightFeaturedView.click_search_button()
        baseSetUp.check_result_string(actualResult, "Go")
        time.sleep(3)

    def test_SearchFeaturedValid_TC16(self):
        self.test_ClickSearchFeaturedAppear_TC16n17()
        self.flightFeaturedView.set_field_dropbox("All fields")
        self.flightFeaturedView.set_no_dropBox("1")
        self.flightFeaturedView.set_input_box("American Airlines")
        actualResult = self.flightFeaturedView.click_on_go()
        baseSetUp.check_result_string(actualResult, "Reset")
        time.sleep(6)

    def test_Reset_button(self):
        self.test_SearchFeaturedValid_TC16()
        time.sleep(3)
        actualResult = self.flightFeaturedView.click_on_reset()
        baseSetUp.check_result_string(actualResult, "mainpage")
        time.sleep(3)

    # ************************************************************ search end****************************************

    # *******************************************************************************************************************************************************

    # *********************************************************** Add Airport Test Cases ***************************

    def FeaturedValues(self):#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.test_AddNewFeaturedPageAppear_TC2()
        self.flightFeaturedAdd = FlightFeatured.AddFlightFeatured(SetUp.driver)
        self.flightFeaturedAdd.set_status("Enabled")
        self.flightFeaturedAdd.set_airline("Bangladesh Airline")
        self.flightFeaturedAdd.set_from_airport("BNG")
        self.flightFeaturedAdd.set_to_airport("04G")
        self.flightFeaturedAdd.set_price("1000")

    def test_AddANewFeaturedValid_TC2(self):#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.FeaturedValues()
        self.flightFeaturedAdd.click_on_save()
        time.sleep(4)

    def test_AddWithoutValue_TC2(self):#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.test_AddNewFeaturedPageAppear_TC2()
        self.flightFeaturedAdd = FlightFeatured.AddFlightFeatured(SetUp.driver)
        self.flightFeaturedAdd.set_status("")
        self.flightFeaturedAdd.set_airline("")
        self.flightFeaturedAdd.set_from_airport("")
        self.flightFeaturedAdd.set_to_airport("")
        self.flightFeaturedAdd.set_price("")
        self.flightFeaturedAdd.click_on_save()

    def test_AddSameFeaturedTwice_TC4(self):
        self.FeaturedValues()
        self.flightFeaturedAdd.click_on_save()

        actualResult = self.flightFeaturedAdd.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Flight Already exits")
        time.sleep(3)

    def test_PriceInput_TC5(self):
        self.FeaturedValues()
        self.flightFeaturedAdd.set_price("1gjhghffx")
        self.flightFeaturedAdd.click_on_save()

        actualResult = self.flightFeaturedAdd.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Invalid input")
        time.sleep(3)



    @classmethod
    def tearDownClass(cls):
        SetUp.driver.close()

    if __name__ == '__main__':
        unittest.main()
