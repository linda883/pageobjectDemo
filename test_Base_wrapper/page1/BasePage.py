from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver, base_url, page_title):
        self.browser: WebDriver = driver
        self.base_url = base_url
        self.page_title = page_title

    def on_page(self, page_title):
        return page_title in self.browser.title

    def _open(self, url, page_title):
        self.browser.get(url)
        self.browser.maximize_window()
        assert self.on_page(page_title), "打开页面失败%s" % url

    def find_element(self, *loc):
        # return self.browser.find_element(*loc)
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(loc))
            return self.browser.find_element(*loc)
        except AttributeError:
            print("%s页面中未能找到%s元素" % (self, loc))

    def switch_frame(self, name):
        return self.browser.switch_to.frame(name)

    def js_script(self, src):
        self.browser.execute(src)

    def send_keys(self, loc, keyword, clear_c=True, click_c=True):
        try:
            loc = getattr(self, "_%s" % loc) #self.loc
            if click_c:
                self.find_element(*loc).click()
            if clear_c:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(keyword)
        except AttributeError:
            print("%s页面中未能找到%s元素" % (self, loc))

