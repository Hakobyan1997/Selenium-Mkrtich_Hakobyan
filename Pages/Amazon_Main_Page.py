from Locators import Locators
from selenium.webdriver.common.keys import Keys
from Common.CustomFind import Find
from Pages.BasePage import BasePageClass



class Amazon_Main_Page(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators.LocatorsClass()

    def click_search_field(self):
        search_field_path = self.find_element(self.locators.search_field_path)
        search_field_path.click()
        search_field_path.send_keys("adidas cap for men")
        search_field_path.send_keys(Keys.ENTER)
