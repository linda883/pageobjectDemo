from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BaiduIndexPage(object):
    # 初始化方法，调用类时执行，一般进行准备工作。
    # driver浏览器
    def __init__(self, driver):
        self.driver:WebDriver = driver
        # 百度搜索框的定位方式：属性
        # 定位使用括号，元组
        self.search_textbox_id = (By.ID, "kw")
        self.b_submit_button_id = (By.ID, "su")

        # 输入关键字方法,通过参数soso_text传入
    def enter_search_text(self, soso_text):
        self.driver.find_element(*self.search_textbox_id).click()
        self.driver.find_element(*self.search_textbox_id).clear()
        self.driver.find_element(*self.search_textbox_id).send_keys(soso_text)

        # 点击百度一下的方法
    def click_baiduyixia(self):
        self.driver.find_element(*self.b_submit_button_id).click()

