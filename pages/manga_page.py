from selenium.webdriver.common.by import By


class Manga:
    SELECT_MANGA = (By.XPATH, "//*[@id='manga-list-container']/div[4]//div[2]/div[1]/a")
    SORTED_BUTTON = (By.XPATH, "//*[@id='sorter-sort']")
    CHOOSE_SORTED = (By.XPATH, "//*[@id='sorter']//div[1]/div[3]//span[3]")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://animego.org/manga")

    def choose_manga_in_list(self):
        element = self.driver.find_element(*Manga.SELECT_MANGA)
        element.click()
        assert self.driver.current_url == "https://animego.org/manga/keyon-shaffl-1795"

    def sorted_manga(self):
        element = self.driver.find_element(*Manga.SORTED_BUTTON)
        element.click()
        element_2 = self.driver.find_element(*Manga.CHOOSE_SORTED)
        element_2.click()
        assert self.driver.current_url == "https://animego.org/manga?sort=r.rating&direction=desc"
