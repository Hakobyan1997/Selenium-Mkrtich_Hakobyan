import time
import unittest
from selenium import webdriver
from Pages import Amazon_Main_Page
from Pages import Login_Page
from Pages import Password_Page
from Pages import Product_Details_Page
from Pages import Search_Results_Page
from Pages import BasePage
from Pages  import Cart_Page
from Pages import Shopping_Cart_Page
from TestCases.BaseTest import BaseTestClass


class ParcelQuantity(BaseTestClass):
    def setUp(self):
        self.logger.add_log("INFO", "___________________________________")
        self.Amazon_Main_Page = Amazon_Main_Page.Amazon_Main_Page(self.driver)
        self.Login_Page = Login_Page.LoginPage(self.driver)
        self.Password_Page = Password_Page.PasswordPage(self.driver)
        self.Product_Details_Page = Product_Details_Page.Product_Details_Page(self.driver)
        self.Search_Results_Page = Search_Results_Page.Search_Results_Page(self.driver)
        self.BasePage = BasePage.BasePageClass(self.driver)
        self.Shopping_Cart_Page = Shopping_Cart_Page.Indicate_quantity_item(self.driver)
        self.Cart_Page = Cart_Page.Cart_Page(self.driver)

    def test_Indicate_The_Quantity_Of_The_Parcel_Page(self):
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
        self.Cart_Page.click_shopping_cart_button()
        time.sleep(3)
        self.Shopping_Cart_Page.click_quantity_button()
        time.sleep(2)
        self.Shopping_Cart_Page.change_quantity_number_to_7()
        time.sleep(2)
        self.logger.add_log("INFO", "Test Case '{}' Finished ".format(type(self).__name__))


    # def tearDown(self):
    #     self.driver.close()

if __name__ == "__main__":
    unittest.main()
