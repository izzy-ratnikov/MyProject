from helper import ANIME_LIST_URL
from pages.base_page import BasePage


class AnimeListLocators:
    CHOOSE_ANIME = '//*[@id="anime-list-container"]/div[5]/div/div[2]/div[1]/a'


class AnimeList(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(ANIME_LIST_URL)
        super().__init__(driver)

    def choose_anime_from_list(self):
        base_page = BasePage(self.driver)
        return base_page.click_on(AnimeListLocators.CHOOSE_ANIME)
