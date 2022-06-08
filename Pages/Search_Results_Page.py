from Locators import Locators
from Common.CustomFind import Find
from Pages.BasePage import BasePageClass

class Search_Results_Page(BasePageClass):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = Locators.LocatorsClass()

    def click_to_product(self):
        selected_product_path = self.find_element(self.locators.selected_product_path)
        selected_product_path.click()
