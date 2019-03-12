from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class sosoResultPage():

    def __init__(self, driver):
        self.driver:WebDriver = driver
        '''
        driver: webdriver
        '''

        self.ss_text_xpath = (By.XPATH, "//*[@id='1']/h3/a")

    def get_sstext(self):
        return self.driver.find_element(*self.ss_text_xpath).text

