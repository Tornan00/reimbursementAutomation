from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

class reimbursementSubmissionPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def amount_field(self):
        element: WebElement = self.driver.find_element_by_id("amountInput")
        return element

    def category_field(self):
        element: Select = Select(self.driver.find_element_by_id("categories"))
        return element

    def desc_field(self):
        element: WebElement = self.driver.find_element_by_id("descArea")
        return element

    def submission_button(self):
        element: WebElement = self.driver.find_element_by_id("submitButton")
        return element

    def reimbursement_table_body(self):
        #element: WebElement = self.driver.find_element_by_id("tableBody")
        elements: List[WebElement] = self.driver.find_elements_by_xpath("//table/tbody/tr")
        return elements