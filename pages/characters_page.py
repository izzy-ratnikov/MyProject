from selenium.webdriver.common.by import By

from helper import CHARACTERS_URL
from pages.base_page import BasePage


class CharactersLocators:
    SELECT_CHARACTER = "//*[@id='anime-list-container']/div[10]/div/div[2]/h3/a"


class Characters(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.driver.get(CHARACTERS_URL)

    def choose_character_in_list(self):
        base_page = BasePage(self.driver)
        return base_page.get_locator_xpath(CharactersLocators.SELECT_CHARACTER).click()

