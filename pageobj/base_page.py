import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_url(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def wait_for_title(self, title, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.title_is(title))

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.higlight_locator(locator)
        self.wait_for_clickable(locator).click()

    def click_and_ignore_error(self,locator):
        try:
            self.wait_for_clickable(locator).click()
        except:
            print("Ignore error messgae")

    def type(self, locator, text):
        self.wait_for_element(locator)
        self.clear(locator)
        self.higlight_locator(locator)
        self.get_element(locator).send_keys(text)

    def clear(self, locator):
        self.get_element(locator).clear()

    def navigate_to(self, url):
        self.driver.get(url)

    def close_browser(self):
        self.driver.quite()

    def swith_to_frame(self,name):
        self.driver.switch_to.frame(name)

    def javascript_click(self,locator):
        self.higlight_locator(locator)
        elm= self.get_element(locator)
        # perform click with execute_script
        self.driver.execute_script("arguments[0].click();", elm);
    def verify_page_should_contain(self,value):
        try:
            self.driver.find_element(By.XPATH,f"//*[contains(text(),'{value}')]")
        except:
            raise AssertionError(f"Element text is not present :{value}")
    def screenshot(self,name):
        self.driver.save_screenshot(f"{name}.png")

    def higlight_locator(self,locator):
        element = self.get_element(locator)
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='2px solid green'", element)