import time
import unittest
from Base import SetUp
from Pages import FlightsAll, DashBoard

baseSetUp = SetUp.MyTestCase()


class FlightsAllTesCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        baseSetUp.setUp()
        baseSetUp.admin_login()
        this_class = FlightsAllTesCases()
        cls.page_objects(this_class)
        cls.test_ModuleStatus(this_class)
        cls.test_flightPageAppear_TC1(this_class)

    def setUp(self):
        self.page_objects()

    def page_objects(self):
        self.dashboard = DashBoard.DashBoard(baseSetUp.driver)
        self.flight = FlightsAll.FlightView(baseSetUp.driver)
        self.flightAdd = None
        self.flightEdit = None

    # *************************************View Section test Cases***********************************************************************************
    def test_ModuleStatus(self):
        self.dashboard.goto_Modules()
        self.flight.click_module_flight_status()
        time.sleep(2)

    def test_flightPageAppear_TC1(self):
        # self.test_ModuleStatus()
        self.dashboard.goto_all_flights()
        self.dashboard.goto_flights()
        pageTittle = baseSetUp.driver.title
        # print(pageTittle)
        baseSetUp.check_result_string(pageTittle, "Flights")

    def test_AddNewFlightOptionAppear_TC2(self):
        # self.test_flightPageAppear_TC1()
        self.flight.click_add_button()
        time.sleep(10)
        pageStart = self.flight.get_AddFlight_identifier()
        # print(pageStart)
        baseSetUp.check_result_string(pageStart, "Status")

    def test_EditButton_TC14(self):
        # self.test_flightPageAppear_TC1()
        self.flight.click_edit_button(0)
        time.sleep(6)
        pageStart = self.flight.get_EditFlight_identifier()
        print(pageStart)
        baseSetUp.check_result_string(pageStart, "Status")

    def test_DeleteButton_TC10(self):
        # self.test_flightPageAppear_TC1()
        self.flight.click_delete_button(0, "yes")
        time.sleep(3)

    def test_StatusChange_TC8(self):
        # self.test_flightPageAppear_TC1()
        status = self.flight.click_satus(0)
        time.sleep(2)
        if status == "ok":
            actualResult = self.flight.get_text_popup()
            baseSetUp.check_result_string(actualResult,
                                          "Info Updated\n" + "Information updated successfully")

        time.sleep(6)

    def test_ClickCheckbox_TC9(self):
        # self.test_flightPageAppear_TC1()
        actualResult = self.flight.click_checkbox(0)
        if actualResult != "no":
            baseSetUp.check_result_string(actualResult, "deleteAll")
            time.sleep(3)

    def test_DeleteAll_TC15(self):  # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.test_ClickCheckbox_TC9()
        self.flight.click_checkbox_all()
        actualResult = self.flight.click_delete_all("yes")

    # **************************************************Flight search section Test Cases*************************
    def test_ClickSearchFlightBoxAppear_TC16n17(self):
        # self.test_flightPageAppear_TC1()
        actualResult = self.flight.click_search_button()
        baseSetUp.check_result_string(actualResult, "Go")
        time.sleep(3)

    def test_SearchFlightValid_TC16(self):
        self.test_ClickSearchFlightBoxAppear_TC16n17()
        self.flight.set_field_dropdown("User id")
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

    def test_Reset_button(self):
        self.test_SearchFlightValid_TC16()
        time.sleep(3)
        actualResult = self.flight.click_on_reset()
        baseSetUp.check_result_string(actualResult, "mainpage")
        time.sleep(3)

    def test_SearchFlightInvalid_TC17(self):
        self.test_ClickSearchFlightBoxAppear_TC16n17()
        self.flight.set_field_dropdown("User id")
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

    def test_Back_button(self):
        # self.test_flightPageAppear_TC1()
        actualResult = self.flight.click_back_button()
        baseSetUp.check_result_string(actualResult, "Dashboard")
        time.sleep(3)

    # ************************************************************ search end****************************************

    # *******************************************************************************************************************************************************

    # *********************************************************** Add Flights Test Cases ***************************

    def FlightValues(self):
        self.test_AddNewFlightOptionAppear_TC2()
        self.flightAdd = FlightsAll.FlightAdd(baseSetUp.driver)
        self.flightAdd.set_status("Enabled")
        self.flightAdd.set_airline("Air Bangladesh")
        self.flightAdd.set_id("supplier@phptravels.com")
        self.flightAdd.set_airport_from("CTG_1")
        self.flightAdd.set_airport_to("DHK-1")
        self.flightAdd.set_duration("3H")
        self.flightAdd.set_type("Economy")
        self.flightAdd.set_refundable("Disable")
        self.flightAdd.set_departure_time()
        self.flightAdd.set_arrival_time()
        self.flightAdd.set_baggage("5")
        self.flightAdd.set_cabin_baggage("3")

        self.flightAdd.set_adult_price("1000")
        self.flightAdd.set_child_price("500")
        self.flightAdd.set_infant_price("90")

    def test_AddANewFlightValid_TC2(self):
        self.FlightValues()
        self.flightAdd.click_on_save()
        actualResult = self.flight.get_first_element_from_table()
        print(actualResult)
        expectedResult = ('supplier@phptravels.com', 'Air Bangladesh', 'CTG_1', 'DHK-1')
        baseSetUp.check_result_string(actualResult, expectedResult)
        time.sleep(4)

    def test_AddWithoutValue_TC2(self):
        self.test_AddNewFlightOptionAppear_TC2()
        self.flightAdd = FlightsAll.FlightAdd(baseSetUp.driver)
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
        actualResult = self.flight.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Invalid input")
        time.sleep(6)

    def test_AddSameFlightTwice_TC4(self):
        self.FlightValues()
        self.flightAdd.click_on_save()

        actualResult = self.flight.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Flight Already exits")
        time.sleep(6)

    def test_AddFlightInvalid_TC5(self):
        self.FlightValues()
        self.flightAdd.set_airport_from("04C")
        self.flightAdd.set_airport_to("04G")
        self.flightAdd.click_on_save()

        actualResult = self.flight.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Invalid input")
        time.sleep(6)

    def test_AddFlight_PriceInput_TC6(self):
        self.FlightValues()
        self.flightAdd.set_adult_price("107bdshfg")
        self.flightAdd.set_child_price("788dfjasg")
        self.flightAdd.set_infant_price("9dsfjdshfkj")
        self.flightAdd.click_on_save()

        actualResult = self.flight.get_text_popup()
        baseSetUp.check_result_string(actualResult, "Invalid input")
        time.sleep(6)

    def test_AddFlight_TimeInput_TC7(self):
        self.FlightValues()
        self.flightAdd.click_on_save()

        firstFlight = self.flight.get_first_flight_from_table()
        print(firstFlight)
        baseSetUp.check_result_string(firstFlight, "supplier@phptravels.com")
        time.sleep(2)
        # ************************************************end of Add Flight Test Cases ***************************************

        # **************************************************Edit Flight Test Cases *********************************************

    def before(self):
        self.test_EditButton_TC14()
        self.flightEdit = FlightsAll.FlightEdit(baseSetUp.driver)

    def FlightValuesEdit(self):
        self.before()
        self.flightAdd.set_status("Enabled")
        self.flightAdd.set_airline("12 North")
        self.flightAdd.set_id("supplier@phptravels.com")
        self.flightAdd.set_airport_from("06C")
        self.flightAdd.set_airport_to("04G")
        self.flightAdd.set_duration("45")
        self.flightAdd.set_type("Economy")
        self.flightAdd.set_refundable("Disable")
        self.flightAdd.set_departure_time()
        self.flightAdd.set_arrival_time()
        self.flightAdd.set_baggage("3")
        self.flightAdd.set_cabin_baggage("5")

        self.flightAdd.set_adult_price("1000")
        self.flightAdd.set_child_price("500")
        self.flightAdd.set_infant_price("90")

    def test_EditFlightValid_TC10(self):
        self.FlightValuesEdit()
        self.flightAdd.click_on_save()

    def test_EditFlightInvalid_TC12(self):
        self.FlightValuesEdit()
        self.flightAdd.set_adult_price("hsdjdfh")
        self.flightAdd.set_child_price("dsah")
        self.flightAdd.click_on_save()

    def test_SaveWithOutChange_TC11(self):
        self.before()
        self.flightAdd.click_on_save_route()
        pageTittle = baseSetUp.driver.title
        baseSetUp.check_result_string(pageTittle, "Flights")
        pass

    def test_AddtButton_TC10(self):
        self.before()
        actualResult = self.flightEdit.click_add_route()
        baseSetUp.check_result_string(actualResult, "airport")
        time.sleep(6)

    def test_add_FlightsRute_TC10(self):
        self.test_AddtButton_TC10()
        self.flightEdit.set_airport_route("04G")
        self.flightEdit.set_arrival_time_route()
        self.flightEdit.set_departure_time_route()
        self.flightEdit.set_duration_route(4)
        self.flightEdit.click_on_save_route()

    def test_ExportButton_TC10(self):
        self.before()
        actualResult = self.flightEdit.click_export()
        baseSetUp.check_result_string(actualResult, "https://phptravels.net/admin/xcrud/xcrud_ajax.php")
        time.sleep(6)

    @classmethod
    def tearDownClass(cls):
        baseSetUp.driver.close()

    if __name__ == '__main__':
        unittest.main()


def suit():
    test_suit = unittest.TestSuite()
    test_suit.addTest(FlightsAllTesCases("test_StatusChange_TC8"))
    test_suit.addTest(FlightsAllTesCases("test_DeleteButton_TC10"))
    test_suit.addTest(FlightsAllTesCases("test_DeleteAll_TC15"))
    test_suit.addTest(FlightsAllTesCases("test_Reset_button"))
    return test_suit
