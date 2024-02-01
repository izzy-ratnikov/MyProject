from selenium.webdriver.common.by import By


class AnimePage:
    STAR_RATING = (By.CSS_SELECTOR, ".star-rating.mr-2")
    BUTTON_PLAY_TRAILER = (By.XPATH, "//*[@id='content']/div/div[3]/div/div[2]/div[2]/a")
    CHOOSE_RELATED = (By.XPATH, "//*[@id='video-watch2']/div[1]//div/div[1]/a")

    def __init__(self, driver):
        self.driver = driver

    def watch_trailer_anime(self):
        self.driver.get('https://animego.org/anime/magiya-i-muskuly-2-2493')
        element = self.driver.find_element(*AnimePage.BUTTON_PLAY_TRAILER)
        element.click()
        assert element.get_attribute('href') in '"https://www.youtube.com/embed/zk0YBvw53MI"'

    def related_anime(self):
        self.driver.get('https://animego.org/anime/agent-vremeni-2-2343')
        element = self.driver.find_element(*AnimePage.CHOOSE_RELATED)
        element.click()
        assert self.driver.current_url == "https://animego.org/anime/agent-vremeni-1780"
