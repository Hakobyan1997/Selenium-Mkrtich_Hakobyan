import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Common.Logger.LoggerFile import LoggerClass
from Common.Variables import Variables



class BaseTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.delete_all_cookies()
        cls.driver.maximize_window()
        cls.variables = Variables.ProjectVariables()
        cls.logger = LoggerClass()

    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()
        cls.driver.quit()

