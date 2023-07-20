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
    def test_ModuleStatus(self):
        self.dashboard.goto_Modules()
        self.flightFeaturedView.click_module_flight_status()
        time.sleep(2)

    def test_FightFeaturedPageAppear(self):
        self.test_ModuleStatus()
        self.dashboard.goto_all_flights()
        self.dashboard.goto_featured_flight()
        time.sleep(3)
        pageTittle = SetUp.driver.title
        # print(pageTittle)
        baseSetUp.check_result_string(pageTittle, "Flights Featured")

    def test_AddNewFeaturedPageAppear(self):
        self.test_FightFeaturedPageAppear()
        pageStart = self.flightFeaturedView.click_Add_button()
        baseSetUp.check_result_string(pageStart, "Status")

    def test_EditButton(self):
        pass

    def test_DeleteButton(self):
        self.test_FightFeaturedPageAppear()
        self.flightFeaturedView.click_delete_button(0, "yes")
        time.sleep(3)

    def test_StatusChange(self):
        self.test_FightFeaturedPageAppear()
        self.flightFeaturedView.click_satus(0)
        time.sleep(2)
        actualResult = self.flightFeaturedView.get_text_popup()
        baseSetUp.check_result_string(actualResult,
                                      "Info Updated\n" + "Information updated successfully")
        time.sleep(6)

    def test_ClickCheckbox(self):
        self.test_FightFeaturedPageAppear()
        actualResult = self.flightFeaturedView.click_checkbox(0)
        baseSetUp.check_result_string(actualResult, "deleteAll")
        time.sleep(3)

    def test_DeleteAll(self):
        self.test_FightFeaturedPageAppear()
        self.flightFeaturedView.click_checkbox_all()
        actualResult = self.flightFeaturedView.click_delete_all("yes")
        baseSetUp.check_result_string(actualResult, 1)

    # **************************************************Flight search section Test Cases*************************
    def test_ClickSearchFeaturedAppear(self):
        self.test_FightFeaturedPageAppear()
        actualResult = self.flightFeaturedView.click_search_button()
        baseSetUp.check_result_string(actualResult, "Go")
        time.sleep(3)

    def test_SearchFeaturedValid(self):
        self.test_ClickSearchFeaturedAppear()
        self.flightFeaturedView.set_field_dropbox("All fields")
        self.flightFeaturedView.set_no_dropBox("1")
        self.flightFeaturedView.set_input_box("American Airlines")
        actualResult = self.flightFeaturedView.click_on_go()
        baseSetUp.check_result_string(actualResult, "Reset")
        time.sleep(6)

    def test_Reset_button(self):
        self.test_SearchFeaturedValid()
        time.sleep(3)
        actualResult = self.flightFeaturedView.click_on_reset()
        baseSetUp.check_result_string(actualResult, "mainpage")
        time.sleep(3)

    # ************************************************************ search end****************************************

    # *******************************************************************************************************************************************************

    # *********************************************************** Add Airport Test Cases ***************************

    def FeaturedValues(self):
        self.test_AddNewFeaturedPageAppear()
        self.flightFeaturedAdd = FlightFeatured.AddFlightFeatured(SetUp.driver)
        self.flightFeaturedAdd.set_status("Enabled")
        self.flightFeaturedAdd.set_airline("135 Airways")
        self.flightFeaturedAdd.set_from_airport("CTG_1")
        self.flightFeaturedAdd.set_to_airport("DHK-1")
        self.flightFeaturedAdd.set_price("3000")

    def test_AddANewFeaturedValid(self):
        self.FeaturedValues()
        self.flightFeaturedAdd.click_on_save()
        actualResult = self.flightFeaturedView.get_first_element_from_table()
        print(actualResult)
        expectedResult = ('135 Airways', 'CTG_1', 'DHK-1')
        baseSetUp.check_result_string(actualResult, expectedResult)
        time.sleep(4)

    def test_AddWithoutValue(self):
        self.test_AddNewFeaturedPageAppear()
        self.flightFeaturedAdd = FlightFeatured.AddFlightFeatured(SetUp.driver)
        self.flightFeaturedAdd.set_status("")
        self.flightFeaturedAdd.set_airline("")
        self.flightFeaturedAdd.set_from_airport("")
        self.flightFeaturedAdd.set_to_airport("")
        self.flightFeaturedAdd.set_price("")
        self.flightFeaturedAdd.click_on_save()

    def test_AddSameFeaturedTwice(self):
        self.FeaturedValues()
        self.flightFeaturedAdd.click_on_save()

        actualResult = self.flightFeaturedAdd.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Flight Already exits")
        time.sleep(3)

    def test_PriceInput(self):
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
