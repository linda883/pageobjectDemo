from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_fz_base.page2.BasePage import BasePage


class BaiduIndexPage(BasePage):

    search_textbox_id = (By.ID, "kw")
    b_submit_button_id = (By.ID, "su")

    def open(self):
        self._open(self.base_url, self.page_title)

        # 输入关键字方法,通过参数soso_text传入
    def enter_search_text(self, soso_text):
        self.find_element(*self.search_textbox_id).send_keys(soso_text)

        # 点击百度一下的方法
    def click_baiduyixia(self):
        self.find_element(*self.b_submit_button_id).click()

