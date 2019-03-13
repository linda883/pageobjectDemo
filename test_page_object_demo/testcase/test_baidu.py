# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from test_page_object_demo.page.BaiduIndexPage import BaiduIndexPage
from test_page_object_demo.page.BaiduSouResultPage import sosoResultPage


class TestBaiduIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 打开浏览器
        cls.driver = webdriver.Chrome(executable_path='/Users/lindafang/PycharmProjects/pageobjectDemo/chromedriver')
        # 等待页面加载直到出现
        cls.driver.implicitly_wait(30)

    def test_app_dynamics_job(self):
        # 打开一个浏览器（通过代码+浏览器驱动）
        driver = self.driver
        # 打开你要测试的主页
        driver.get("https://www.baidu.com/")

        # BaiduIndexPage实例sobd，主页加载打开
        sobd = BaiduIndexPage(driver)
        # 输入搜索内容
        sobd.enter_search_text("pageobject")
        # 点击
        sobd.click_baiduyixia()
        time.sleep(2)
        # 页面切换到查询结果页
        result_page = sosoResultPage(driver)
        # 获得结果
        res_text = result_page.get_sstext()
        # 验证结果是否正确
        self.assertIn("pageobject", driver.title)
        self.assertIn("PageObject", res_text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('测试结束了，OK')


if __name__ == "__main__":
    unittest.main()
