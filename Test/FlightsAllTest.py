import time
import unittest
#dropdown error
from Base import SetUp
from Pages import FlightsAll, DashBoard

baseSetUp = SetUp.MyTestCase()


class FlightsAllTesCases(unittest.TestCase):

    def setUp(self):
        # baseSetUp.test_before_run()
        baseSetUp.setUpClass()
        baseSetUp.setUp()
        self.page_objects()

    def page_objects(self):
        self.dashboard = DashBoard.DashBoard(SetUp.driver)
        self.flight = FlightsAll.FlightView(SetUp.driver)

    # *************************************View Section test Cases******************
    def test_flightPageAppear_TC1(self):
        self.dashboard.goto_all_flights()
        self.dashboard.goto_flights()

    def test_AddNewFlightOptionAppear_TC2(self):
        self.test_flightPageAppear_TC1()
        self.flight.click_add_button()
        time.sleep(6)

    def test_EditButton_TC10(self):
        self.test_flightPageAppear_TC1()
        self.flight.click_edit_button(0)
        time.sleep(6)

    def test_DeleteButton_TC10(self):
        self.test_flightPageAppear_TC1()
        self.flight.click_delete_button(0)
        time.sleep(6)

    def test_StatusChange_TC8(self):
        self.test_flightPageAppear_TC1()
        self.flight.click_satus(0)
        time.sleep(6)

    def test_ClickCheckbox_TC9(self):
        self.test_flightPageAppear_TC1()
        self.flight.click_checkbox(0)
        time.sleep(6)

    def test_SearchFlightBoxAppear_TC16n17(self):
        self.test_flightPageAppear_TC1()
        self.flight.click_search_button()
        time.sleep(6)

    def test_SearchFlightValid_TC16(self):
        self.test_SearchFlightBoxAppear_TC16n17()
        self.flight.set_field_dropdown("Status")



    @classmethod
    def tearDownClass(cls):
        SetUp.driver.close()

    if __name__ == '__main__':
        unittest.main()
