from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.anime_page import AnimePage


class MainPage:
    BUTTON_ANIME = (By.XPATH, "//*[@class='nav-link']")
    CHARACTERS = (By.LINK_TEXT, "Персонажи")
    RANDOM_ANIME = (By.LINK_TEXT, 'Случайное аниме')
    SEARCH_STRING = (By.CSS_SELECTOR, '#navbar-search')
    GENRES = (By.XPATH, "//*[@id='filter']/div[2]//div[2]/div[2]/button")
    CHOOSE_GENRES = (By.XPATH, "//*[@id='filter']/div[2]//span[7]/span")
    TYPE = (By.XPATH, "//*[@id='filter']/div[2]//div[3]/div[2]/button")
    CHOOSE_TYPE = (By.XPATH, "//*[@id='filter']/div[2]//div[3]//label[1]/span")
    TYPE_OF_VOICE_ACTING = (By.XPATH, "//*[@id='filter']/div[2]//div[4]/div[2]/button")
    CHOOSE_VOICE_ACTING = (By.XPATH, "//*[@id='filter']/div[2]//div[4]//label[1]/span")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='filter']/div[2]//div[8]/button")
    LINE_DATE = (By.XPATH, "//*[@id='slider-range']")

    def __init__(self, driver):
        self.driver = driver

    def find_url_anime(self):
        element = self.driver.find_element(*MainPage.BUTTON_ANIME)
        assert element.get_attribute('href') in 'https://animego.org/anime'

    def find_button_anime(self):
        element = self.driver.find_element(*MainPage.BUTTON_ANIME)
        assert element.text == "Аниме"

    def click_on_button_anime(self):
        element = self.driver.find_element(*MainPage.BUTTON_ANIME)
        element.click()
        assert self.driver.current_url == 'https://animego.org/anime'

    def click_on_button_characters(self):
        element = self.driver.find_element(*MainPage.CHARACTERS)
        element.click()
        assert self.driver.title == 'Список аниме персонажей'

    def click_button_random_anime(self):
        element = self.driver.find_element(*MainPage.RANDOM_ANIME)
        element.click()
        assert self.driver.find_element(*AnimePage.STAR_RATING)

    def write_on_search_string(self, text):
        element = self.driver.find_element(*MainPage.SEARCH_STRING)
        element.click()
        element.send_keys(text)
        element.send_keys(Keys.RETURN)
        assert self.driver.current_url == "https://animego.org/search/all?q=91+день" or "https://animego.org/search/all?q=магическая+битва" or "https://animego.org/search/all?q=тетрадь+смерти"

    def choose_anime_with_filters(self):
        element = self.driver.find_element(*MainPage.GENRES)
        element.click()
        element_2 = self.driver.find_element(*MainPage.CHOOSE_GENRES)
        element_2.click()
        element_3 = self.driver.find_element(*MainPage.TYPE)
        element_3.click()
        element_4 = self.driver.find_element(*MainPage.CHOOSE_TYPE)
        element_4.click()
        element_5 = self.driver.find_element(*MainPage.TYPE_OF_VOICE_ACTING)
        element_5.click()
        element_6 = self.driver.find_element(*MainPage.CHOOSE_VOICE_ACTING)
        element_6.click()
        element_7 = self.driver.find_element(*MainPage.SEARCH_BUTTON)
        element_7.click()
        assert self.driver.current_url == "https://animego.org/anime/filter/genres-is-mystery/type-is-tv/dubbing-is-anilibria/apply"

    def search_anime_by_date(self):
        line_date = self.driver.find_element(*MainPage.LINE_DATE)
        line_date.click()
        element = self.driver.find_element(*MainPage.SEARCH_BUTTON)
        element.click()
        assert self.driver.current_url == "https://animego.org/anime/filter/year-from-1991/apply"
