from Locators import Locators
from Common.CustomFind import Find
from Pages.BasePage import BasePageClass


class Sign_Out_Page(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators.LocatorsClass()

    def click_all_button(self):
        all_button = self.find_element(self.locators.all_button)
        all_button.click()

    def click_sign_out_button(self):
        sign_out_button = self.find_element(self.locators.sign_out_button)
        sign_out_button.click()

