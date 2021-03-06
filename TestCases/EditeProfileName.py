import time
import unittest
from selenium import webdriver
from Pages import Amazon_Main_Page
from Pages import Login_Page
from Pages import Password_Page
from Pages import Product_Details_Page
from Pages import Search_Results_Page
from Pages import Manage_Profile_Page
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from TestCases.BaseTest import BaseTestClass



class Edit_Profile_Name(BaseTestClass):
    def setUp(self):
        self.logger.add_log("INFO", "___________________________________")
        self.Amazon_Main_Page = Amazon_Main_Page.Amazon_Main_Page(self.driver)
        self.Login_Page = Login_Page.LoginPage(self.driver)
        self.Password_Page = Password_Page.PasswordPage(self.driver)
        self.Product_Details_Page = Product_Details_Page.Product_Details_Page(self.driver)
        self.Search_Results_Page = Search_Results_Page.Search_Results_Page(self.driver)
        self.Manage_Profile_Page = Manage_Profile_Page.Manage_Profile(self.driver)

    def test_edit_profile_name(self):
        driver = self.driver
        driver.get("https://www.amazon.com")
        self.Login_Page.fill_login()
        time.sleep(2)
        self.Login_Page.click_to_Continue()
        self.Password_Page.fill_password()
        time.sleep(4)
        self.Password_Page.press_on_keep_me_signed_in_checkbox()
        self.Password_Page.click_to_Sign_in_button()
        time.sleep(4)
        self.Manage_Profile_Page.click_to_account()
        self.Manage_Profile_Page.click_account_link()
        time.sleep(3)
        self.Manage_Profile_Page.click_manage_profile_path()
        self.Manage_Profile_Page.click_edit_account_holder_pencil()
        time.sleep(2)
        self.Manage_Profile_Page.change_profile_name()
        time.sleep(3)
        self.Manage_Profile_Page.click_save_changes_button()
        time.sleep(1)
        self.logger.add_log("INFO", "Test Case '{}' Finished ".format(type(self).__name__))

    # def tearDown(self):
    #     self.driver.close()

if __name__ == "__main__":
    unittest.main()