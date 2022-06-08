import time
import unittest
from selenium import webdriver
from Pages import Amazon_Main_Page
from Pages import Login_Page
from Pages import Password_Page
from Pages import Product_Details_Page
from Pages import Search_Results_Page
from Pages import Sign_Out_Page
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from TestCases.BaseTest import BaseTestClass


class Sign_Out_From_Profile(BaseTestClass):
    def setUp(self):
        self.logger.add_log("INFO", "___________________________________")
        self.logger.add_log("INFO", "___________________________________")
        self.Amazon_Main_Page = Amazon_Main_Page.Amazon_Main_Page(self.driver)
        self.Login_Page = Login_Page.LoginPage(self.driver)
        self.Password_Page = Password_Page.PasswordPage(self.driver)
        self.Product_Details_Page = Product_Details_Page.Product_Details_Page(self.driver)
        self.Search_Results_Page = Search_Results_Page.Search_Results_Page(self.driver)
        self.Sign_Out_Page = Sign_Out_Page.Sign_Out_Page(self.driver)

    def test_search_Amazon(self):
        driver = self.driver
        driver.get("https://www.amazon.com")
        self.Login_Page.fill_login()
        time.sleep(2)
        self.Login_Page.click_to_Continue()
        self.Password_Page.fill_password()
        time.sleep(4)
        self.Password_Page.press_on_keep_me_signed_in_checkbox()
        self.Password_Page.click_to_Sign_in_button()
        time.sleep(3)
        self.Sign_Out_Page.click_all_button()
        time.sleep(4)
        self.Sign_Out_Page.click_sign_out_button()
        time.sleep(3)
        self.logger.add_log("INFO", "Test Case '{}' Finished ".format(type(self).__name__))


    # def tearDown(self):
    #     self.driver.close()

if __name__ == "__main__":
        unittest.main()