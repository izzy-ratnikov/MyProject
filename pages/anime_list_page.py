from selenium.webdriver.common.by import By


class AnimeList:
    CHOOSE_ANIME = (By.XPATH, '//*[@id="anime-list-container"]/div[1]//div[2]/div[1]/a')

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://animego.org/anime")

    def choose_anime_from_list(self):
        element = self.driver.find_element(*AnimeList.CHOOSE_ANIME)
        element.click()
        assert self.driver.current_url == "https://animego.org/anime/vzryvnoy-hrabrec-breyvern-2526"