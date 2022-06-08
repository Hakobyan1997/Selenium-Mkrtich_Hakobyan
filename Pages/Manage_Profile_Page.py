from Locators import Locators
import time
from Common.CustomFind import Find
from Pages.BasePage import BasePageClass
from selenium.webdriver.common.keys import Keys

class Manage_Profile(BasePageClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.locators = Locators.LocatorsClass()
        self.find = Find.FindElementClass(self.driver)

    def click_to_account(self):
        sign_in_to_account = self.find_element(self.locators.sign_in_to_account)
        sign_in_to_account.click()
        time.sleep(3)

    def click_account_link(self):
        my_account_locator = self.find_element(self.locators.my_account_locator)
        my_account_locator.click()

    def click_your_profiles_path(self):
        your_profiles_path = self.find_element(self.locators.your_profiles_path)
        your_profiles_path.click()

    def click_manage_profile_path(self):
        manage_profile_path = self.find_element(self.locators.manage_profile_path)
        manage_profile_path.click()

    def click_edit_account_holder_pencil(self):
        edit_account_holder_path = self.find_element(self.locators.edit_account_holder_path)
        edit_account_holder_path.click()

    def change_profile_name(self):
        profile_name_field_path = self.find_element(self.locators.profile_name_field_path)
        profile_name_field_path.click()
        profile_name_field_path.clear()
        profile_name_field_path.send_keys("Mkrtich")

    def click_save_changes_button(self):
        save_changes_button_path = self.find_element(self.locators.save_changes_button_path)
        save_changes_button_path.send_keys(Keys.ENTER)

