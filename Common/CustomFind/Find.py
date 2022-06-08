from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class FindElementClass():
    def __init__(self, driver):
        self.driver = driver


    def custom_find(self,locator):
        try:
            element = WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except:
            print("Element is not found")
            # exit(2)








