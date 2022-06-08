from Locators import Locators
from Common.CustomFind import Find
from Pages.BasePage import BasePageClass

class LoginPage(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators.LocatorsClass()

    def fill_login(self):
        sign_in_to_account_locator = self.find_element(self.locators.sign_in_to_account)
        sign_in_to_account_locator.click()

        email_path = self.find_element(self.locators.email_path)
        email_path.click()
        email_path.send_keys("mkrtichhakobyan06@gmail.com")

    def click_to_Continue(self):
        continue_button_path = self.find_element(self.locators.continue_button_path)
        continue_button_path.click()

