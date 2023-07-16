import time
import unittest
from Base import SetUp
from Pages import FlightSuggestion, DashBoard

baseSetUp = SetUp.MyTestCase()


class FlightFeaturedTesCases(unittest.TestCase):

    def setUp(self):
        baseSetUp.setUpClass()
        baseSetUp.setUp()
        self.page_objects()

    def page_objects(self):
        self.dashboard = DashBoard.DashBoard(SetUp.driver)
        self.FlightSuggestionView = FlightSuggestion.FlightSuggestionView(SetUp.driver)
        self.FlightSuggestionAdd = None

    # *************************************View Section test Cases***********************************************************************************
    def test_FlightSuggestionPageAppear(self):
        self.dashboard.goto_all_flights()
        self.dashboard.goto_suggestion_flight()
        pageTittle = SetUp.driver.title
        # print(pageTittle)
        baseSetUp.check_result_string(pageTittle, "Flights Suggestions")

    def test_AddNewSuggestionAppear(self):
        self.test_FlightSuggestionPageAppear()
        pageStart = self.FlightSuggestionView.click_Add_button()
        baseSetUp.check_result_string(pageStart, "Status")

    def test_EditButton(self):
        pass

    def test_DeleteButton(self):
        self.test_FlightSuggestionPageAppear()
        self.FlightSuggestionView.click_delete_button(0, "yes")
        time.sleep(3)

    def test_StatusChange(self):
        self.test_FlightSuggestionPageAppear()
        self.FlightSuggestionView.click_satus(0)
        time.sleep(2)
        actualResult = self.FlightSuggestionView.get_text_popup()
        baseSetUp.check_result_string(actualResult,
                                      "Info Updated\n" + "Information updated successfully")
        time.sleep(6)

    def test_ClickCheckbox(self):
        self.test_FlightSuggestionPageAppear()
        actualResult = self.FlightSuggestionView.click_checkbox(0)
        baseSetUp.check_result_string(actualResult, "deleteAll")
        time.sleep(3)

    def test_DeleteAll(self):
        self.test_ClickCheckbox()
        self.FlightSuggestionView.click_checkbox_all()

    # **************************************************Flight search section Test Cases*************************
    def test_ClickSearchSuggestionAppear(self):
        self.test_FlightSuggestionPageAppear()
        actualResult = self.FlightSuggestionView.click_search_button()
        baseSetUp.check_result_string(actualResult, "Go")
        time.sleep(3)

    def test_SearchSuggestionValid(self):
        self.test_ClickSearchSuggestionAppear()
        self.FlightSuggestionView.set_field_dropbox("All fields")
        self.FlightSuggestionView.set_no_dropBox("1")
        self.FlightSuggestionView.set_type_dropbox("")
        self.FlightSuggestionView.set_input_box("JFK")
        actualResult = self.FlightSuggestionView.click_on_go()
        baseSetUp.check_result_string(actualResult, "Reset")
        time.sleep(6)

    def test_Reset_button(self):
        self.test_SearchSuggestionValid()
        time.sleep(3)
        actualResult = self.FlightSuggestionView.click_on_reset()
        baseSetUp.check_result_string(actualResult, "mainpage")
        time.sleep(3)

    # ************************************************************ search end****************************************

    # *******************************************************************************************************************************************************

    # *********************************************************** Add Airport Test Cases ***************************

    def SuggestionValues(self):
        self.test_AddNewSuggestionAppear()
        self.FlightSuggestionAdd = FlightSuggestion.AddFlightSuggestion(SetUp.driver)
        self.FlightSuggestionAdd.set_status("Enabled")
        self.FlightSuggestionAdd.set_type("From_destination")
        self.FlightSuggestionAdd.set_city_airport("CTG_1")
        self.FlightSuggestionAdd.set_order("0")

    def test_AddANewSuggestionValid(self):
        self.SuggestionValues()
        self.FlightSuggestionAdd.click_on_save()
        actualResult = self.FlightSuggestionView.get_first_element_from_table()
        print(actualResult)
        expectedResult = ('from_destination', 'CTG_1')
        baseSetUp.check_result_string(actualResult, expectedResult)
        time.sleep(4)

    def test_AddWithoutValue(self):
        self.test_AddNewSuggestionAppear()
        self.FlightSuggestionAdd = FlightSuggestion.AddFlightSuggestion(SetUp.driver)
        self.FlightSuggestionAdd.set_status(" ")
        self.FlightSuggestionAdd.set_type(" ")
        self.FlightSuggestionAdd.set_city_airport("")
        self.FlightSuggestionAdd.set_order("")
        self.FlightSuggestionAdd.click_on_save()

    def test_AddSameSuggestionTwice(self):
        self.SuggestionValues()
        self.FlightSuggestionAdd.click_on_save()

        actualResult = self.FlightSuggestionAdd.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Flight Already exits")
        time.sleep(3)

    def test_WrongInput(self):
        self.SuggestionValues()
        self.FlightSuggestionAdd.set_order("yt764545")
        self.FlightSuggestionAdd.click_on_save()

        actualResult = self.FlightSuggestionAdd.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Invalid input")
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        SetUp.driver.close()

    if __name__ == '__main__':
        unittest.main()
