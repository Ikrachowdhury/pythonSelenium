from typing import List, Any
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#dropdown error
class ElementsUtil:
    element_array: list[Any]

    def __init__(self, driver):
        self.driver = driver
        self.el = None
        self.length = None
        self.element = None
        self.elements = None
        self.element_array = []

    def element_by_id(self, selector):
        self.element = self.driver.find_element(By.ID, selector)
        return self.element

    def elements_by_class(self, selector):
        self.element = self.driver.find_element(By.CLASS_NAME, selector)
        return self.element

    def element_by_xpath(self, selector):
        self.element = self.driver.find_element(By.XPATH, selector)
        return self.element

    def element_by_css(self, selector):
        self.element = self.driver.find_element(By.CSS_SELECTOR, selector)
        return self.element

    def element_by_name(self, selector):
        self.element = self.driver.find_element(By.NAME, selector)
        return self.element

    def element_by_link(self, selector):
        self.element = self.driver.find_element(By.LINK_TEXT, selector)
        return self.element

    def array_of_table(self, selector_type, selector):
        if selector_type == "class":
            self.elements = self.driver.find_elements(By.CLASS_NAME, selector)
            for element in self.elements:
                self.element_array.append(element)
        return self.element_array

    def get_table_element(self, table, number, child_element):
        try:
            self.length = len(table)
            for i in range(self.length):
                if number == "0":
                    self.element = table[i].find_element(By.CLASS_NAME, child_element)
                else:
                    if self.length > number and i == number:
                        self.element = table[i].find_element(By.CLASS_NAME, child_element)

            return self.element
        except Exception as ex:
            print(ex)

    def dropdown(self, option, element):
        drop_down_element = Select(element)
        drop_down_element.select_by_visible_text(option)
        selected_elements = drop_down_element.all_selected_options
        return [element.text for element in selected_elements]
