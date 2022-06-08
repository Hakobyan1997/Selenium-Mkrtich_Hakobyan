from Locators import Locators
import time
from selenium.webdriver.common.by import By
from Common.CustomFind import Find
from Pages.BasePage import BasePageClass

class  Indicate_quantity_item(BasePageClass):
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators.LocatorsClass()
        self.find = Find.FindElementClass(self.driver)

    def click_quantity_button(self):
        quantity_to_choose_path = self.find_element(self.locators.quantity_to_choose_path)
        quantity_to_choose_path.click()
        time.sleep(2)

    def change_quantity_number_to_7(self):
        quantity_to_choose_number_path = self.find_element(self.locators.quantity_to_choose_number_path)
        quantity_to_choose_number_path.click()


# class Indicate_The_Quantity_Of_The_Parcel_Page:
#     pass