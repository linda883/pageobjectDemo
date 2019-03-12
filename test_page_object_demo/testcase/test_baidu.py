# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from test_page_object_demo.page.BaiduIndexPage import BaiduIndexPage
from test_page_object_demo.page.BaiduSouResultPage import sosoResultPage


class TestBaiduIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        cls.driver = webdriver.Chrome(executable_path='/Users/lindafang/PycharmProjects/pageobjectDemo/chromedriver')
        cls.driver.implicitly_wait(30)

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.baidu.com/")

        # baiduindexpage实例sobd
        sobd = BaiduIndexPage(driver)
        #输入搜索内容
        sobd.enter_search_text("pageobject")
        sobd.click_baiduyixia()
        time.sleep(2)
        result_page = sosoResultPage(driver)
        res_text = result_page.get_sstext()

        self.assertIn("pageobject", driver.title)
        self.assertIn("PageObject", res_text)

    @classmethod
    def tearDownClass(cls):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        cls.driver.close()
        cls.driver.quit()

        print('测试结束了，OK')


if __name__ == "__main__":
    unittest.main()
