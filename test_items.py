from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_chart(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    time.sleep(5)