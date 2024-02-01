from selenium.webdriver.common.by import By


class AnimePage:
    STAR_RATING = (By.CSS_SELECTOR, ".star-rating.mr-2")
    BUTTON_PLAY_TRAILER = (By.XPATH, "//*[@id='content']/div/div[3]/div/div[2]/div[2]/a")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://animego.org/anime/magiya-i-muskuly-2-2493')

    def watch_trailer_anime(self):
        element = self.driver.find_element(*AnimePage.BUTTON_PLAY_TRAILER)
        element.click()
        assert element.get_attribute('href') in '"https://www.youtube.com/embed/zk0YBvw53MI"'

