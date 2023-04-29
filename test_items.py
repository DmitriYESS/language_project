import time

from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."


def test_language_and_add_button(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
