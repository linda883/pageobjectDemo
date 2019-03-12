# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time


class AppDynamicsJob(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        cls.driver = webdriver.Chrome(executable_path='/Users/lindafang/PycharmProjects/pageobjectDemo/chromedriver')
        cls.driver.implicitly_wait(30)

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.baidu.com/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("pageobject")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertIn("pageobject", driver.title)

    @classmethod
    def tearDownClass(cls):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        cls.driver.close()
        cls.driver.quit()

        print('测试结束了，OK')


if __name__ == "__main__":
    unittest.main()
