from pages.base_page import BasePage


class AnimePageLocators:
    STAR_RATING = ".star-rating.mr-2"
    BUTTON_PLAY_TRAILER = "//*[@id='content']/div/div[3]/div/div[2]/div[2]/a"
    CHOOSE_RELATED = "//*[@id='video-watch2']/div[1]//div/div[1]/a"
    TEXT_ANIME_NAME = "//*[@id='content']//div[2]/div[2]//h1"


class AnimePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def watch_trailer_anime(self):
        self.driver.get('https://animego.org/anime/magiya-i-muskuly-2-2493')
        base_page = BasePage(self.driver)
        base_page.click_on(AnimePageLocators.BUTTON_PLAY_TRAILER)
        return base_page.get_attribute(AnimePageLocators.BUTTON_PLAY_TRAILER, 'href')

    def related_anime(self):
        self.driver.get('https://animego.org/anime/agent-vremeni-2-2343')
        base_page = BasePage(self.driver)
        return base_page.get_locator_xpath(AnimePageLocators.CHOOSE_RELATED).click()

    def find_name_anime(self):
        self.driver.get("https://animego.org/anime/magicheskaya-bitva-2-2332")
        base_page = BasePage(self.driver)
        return base_page.get_text(AnimePageLocators.TEXT_ANIME_NAME)
