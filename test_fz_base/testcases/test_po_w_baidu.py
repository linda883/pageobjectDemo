from selenium import webdriver
import unittest

from test_fz_base.page2.BaiduIndexPage import BaiduIndexPage
from test_fz_base.page2.BaiduSouResultPage import SosoResultPage


class TestBaidu1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='/Users/lindafang/PycharmProjects/pageobjectDemo/chromedriver')
        cls.driver.implicitly_wait(30)
        cls.url = "https://www.baidu.com/"

    def setUp(self):
        self.search_text = "pageobject"

    def test_baidu_search(self):
        index_page = BaiduIndexPage(self.driver, self.url, "百度")
        index_page.open()
        index_page.enter_search_text(self.search_text)
        index_page.click_baiduyixia()
        result_page = SosoResultPage(self.driver, self.url, self.search_text)
        assert "PageObject" in result_page.get_sstext()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('测试结束了，OK')


if __name__ == "__main__":
    unittest.main()
