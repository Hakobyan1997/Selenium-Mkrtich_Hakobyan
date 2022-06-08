import time
import unittest
from selenium import webdriver
from Pages import Amazon_Main_Page
from Pages import Login_Page
from Pages import Password_Page
from Pages import Product_Details_Page
from Pages import Search_Results_Page
from Pages import Cart_Page
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from TestCases.BaseTest import BaseTestClass


class Delete_All_Product(BaseTestClass):
    def setUp(self):
        self.logger.add_log("INFO", "___________________________________")
        self.Amazon_Main_Page = Amazon_Main_Page.Amazon_Main_Page(self.driver)
        self.Login_Page = Login_Page.LoginPage(self.driver)
        self.Password_Page = Password_Page.PasswordPage(self.driver)
        self.Product_Details_Page = Product_Details_Page.Product_Details_Page(self.driver)
        self.Search_Results_Page = Search_Results_Page.Search_Results_Page(self.driver)
        self.Cart_Page = Cart_Page.Cart_Page(self.driver)

    def test_delete_all_product_from_cart(self):
        driver = self.driver
        driver.get("https://www.amazon.com")
        self.Login_Page.fill_login()
        time.sleep(6)
        self.Login_Page.click_to_Continue()
        self.Password_Page.fill_password()
        self.Password_Page.press_on_keep_me_signed_in_checkbox()
        time.sleep(6)
        self.Password_Page.click_to_Sign_in_button()
        time.sleep(6)
        self.Cart_Page.click_shopping_cart_button()
        self.Cart_Page.delete_all_product_from_cart()
        time.sleep(10)
        self.logger.add_log("INFO", "Test Case '{}' Finished ".format(type(self).__name__))

    # def tearDown(self):
    #     self.driver.close()

if __name__ == "__main__":
    unittest.main()