from Locators import Locators
from Common.CustomFind import Find
from Pages.BasePage import BasePageClass

class Product_Details_Page(BasePageClass):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = Locators.LocatorsClass()

    def add_to_cart(self):
        add_to_cart_button = self.find_element(self.locators.add_to_cart_button)
        add_to_cart_button.click()

