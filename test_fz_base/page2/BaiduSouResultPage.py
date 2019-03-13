from selenium.webdriver.common.by import By
from test_Base_wrapper.page1.BasePage import BasePage


class SosoResultPage(BasePage):

    ss_text_xpath = (By.XPATH, "//*[@id='1']/h3/a")

    def get_sstext(self):
        return self.find_element(*self.ss_text_xpath).text

