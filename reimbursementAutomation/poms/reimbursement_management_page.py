from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

class reimbursementManagementPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def reason_field(self):
        element: WebElement = self.driver.find_element_by_id("reasonArea")
        return element

    def desc_field(self):
        element: WebElement = self.driver.find_element_by_id("descriptionBox")
        return element

    def deny_button(self):
        element: WebElement = self.driver.find_element_by_id("denyButton")
        return element

    def reimbursement_table_body(self):
        #element: WebElement = self.driver.find_element_by_id("tableBody")
        elements: List[WebElement] = self.driver.find_elements_by_xpath("//table/tbody/tr")
        return elements

    def select_button(self):
        element: WebElement = self.driver.find_element_by_xpath('//*[@id="tableBody"]/tr[1]/td[4]/button')
        return element

    def stats_button(self):
        element: WebElement = self.driver.find_element_by_id("statsButton")
        return element