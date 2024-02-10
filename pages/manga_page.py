from helper import MANGA_URL
from pages.base_page import BasePage


class MangaLocators:
    SELECT_MANGA = "//*[@id='manga-list-container']/div[4]//div[2]/div[1]/a"
    SORTED_BUTTON = "//*[@id='sorter-sort']"
    CHOOSE_SORTED = "//*[@id='sorter']/div/div[1]/div[3]/div/span[3]"


class Manga(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.driver.get(MANGA_URL)

    def choose_manga_in_list(self):
        base_page = BasePage(self.driver)
        base_page.click_on(MangaLocators.SELECT_MANGA)

    def sorted_manga(self):
        base_page = BasePage(self.driver)
        base_page.click_on(MangaLocators.SORTED_BUTTON)
        base_page.click_on(MangaLocators.CHOOSE_SORTED)
