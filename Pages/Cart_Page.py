from Locators import Locators
import time
from selenium.webdriver.common.by import By
from Common.CustomFind import Find
from Pages.BasePage import BasePageClass


class Cart_Page(BasePageClass):
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators.LocatorsClass()
        self.find = Find.FindElementClass(self.driver)

    def click_shopping_cart_button(self):
        shopping_cart_locator = self.find_element(self.locators.shopping_cart_locator)
        shopping_cart_locator.click()

    def delete_product_from_cart(self):
        delete_button_locator = self.find_element(self.locators.delete_button_locator)
        delete_button_locator.click()

    def delete_all_product_from_cart(self):
        all_product = self.find_elements(By.XPATH, "//div[contains(@class, 'a-row sc-list-item')]")
        for x in all_product:
            self.delete_product_from_cart()
            self.driver.refresh()
            time.sleep(2)


