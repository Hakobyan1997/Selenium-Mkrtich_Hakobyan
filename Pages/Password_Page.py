from Locators import Locators
from Common.CustomFind import Find
from Pages.BasePage import BasePageClass


class PasswordPage(BasePageClass):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = Locators.LocatorsClass()

    def fill_password(self):
        password_path = self.find_element(self.locators.password_path)
        password_path.click()
        password_path.send_keys("77494843")

    def press_on_keep_me_signed_in_checkbox(self):
        keep_me_signed_in_checkbox_path = self.find_element(self.locators.keep_me_signed_in_checkbox_path)
        keep_me_signed_in_checkbox_path.click()

    def click_to_Sign_in_button(self):
        sign_in_button_path = self.find_element(self.locators.sign_in_button_path)
        sign_in_button_path.click()

