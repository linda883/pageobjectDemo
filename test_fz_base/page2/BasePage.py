'''
driver,url,findelement,sendkeys
'''
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    # 页面初始化需要的从这传入
    def __init__(self, driver, base_url, page_title):
        self.browser: WebDriver = driver
        self.base_url = base_url
        self.page_title = page_title

# 通过title断言判断页面进入是否正确,True/False
    def on_page(self, page_title):
        return page_title in self.browser.title

    # _开头的方法是私有方法，
    def _open(self, url, page_title):
        self.browser.get(url)
        self.browser.maximize_window()
        assert self.on_page(page_title), "打开页面失败%s" % url

    def find_element(self, *loc):
        # return self.browser.find_element(*loc)
    # 加一个显式的智能等待，元素加载成功
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(loc))
            return self.browser.find_element(*loc)
        except AttributeError:
            print("%s页面中未能找到%s元素" % (self, loc))

    def send_keys(self, loc, keyword, clear_f=True, click_f=True):
        try:
            # getattr相当于实现self.loc(将元组---可调用变量)
            loc = getattr(self, "%s" % loc)
            if click_f:
                self.find_element(*loc).click()
            if clear_f:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(keyword)
        except AttributeError:
            print("%s页面中未能找到%s元素" % (self, loc))

    def switch_frame(self, loc):
        return self.browser.switch_to.frame(loc)

    def js_script(self, src):
        self.browser.execute_script(src)
