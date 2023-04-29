import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."


def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    time.sleep(5)
    try:
        button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert button.is_displayed()
        print("Кнопка найдена и отображается на странице")

    except NoSuchElementException:
        print("Кнопка не найдена на странице")
