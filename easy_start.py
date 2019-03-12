
from selenium import webdriver
import time
#
# 1､打开浏览器(使用代码打开浏览器，需要浏览器的驱动chromedriver)
driver = webdriver.Chrome(executable_path='/Users/lindafang/PycharmProjects/pageobjectDemo/chromedriver')
# 智能等待一会儿
driver.implicitly_wait(30)
# 打开百度首页
driver.get("https://www.baidu.com/")
# 2､在搜索框中输入要查询的信息（“pageobject”）
# 点击
driver.find_element_by_id("kw").click()
# 清除
driver.find_element_by_id("kw").clear()
#  输入信息
driver.find_element_by_id("kw").send_keys("pageobject")

# 3､点击百度一下按钮
driver.find_element_by_id("su").click()
# 4､页面出现查询结果，验证结果是否正确
time.sleep(2)
assert "pageobject" in driver.title
# 5､关闭浏览器
# 关闭当前窗口
driver.close()
# 所有都关掉
driver.quit()