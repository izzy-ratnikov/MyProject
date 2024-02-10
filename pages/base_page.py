from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_text(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        return element.text

    def get_attribute(self, locator, attribute):
        element = self.driver.find_element(By.XPATH, locator)
        return element.get_attribute(attribute)

    def get_locator_xpath(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def click_on(self, locator):
        element = self.get_locator_xpath(locator)
        element.click()

    def get_locator_css(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_locator_link_text(self, locator):
        return self.driver.find_element(By.LINK_TEXT, locator)

    def click_on_css(self, locator):
        element = self.get_locator_css(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.driver.find_element(By.XPATH, locator)
        element.send_keys(text)

    def send_keys_css(self, locator, text):
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        element.send_keys(text)

    def clear_input(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.clear()

    def click_release(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        ActionChains(self.driver).click(element).perform()

    def keyboard_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

    def click_by_js(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)

    def double_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        ActionChains(self.driver).double_click(element).perform()

    def wait_and_click(self, locator, time_out=10):
        try:
            element = WebDriverWait(self.driver, time_out).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
            element.click()
            return element
        except TimeoutException:
            assert False, f"Element {locator} does not find"
