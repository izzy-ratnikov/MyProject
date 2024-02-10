from selenium.webdriver import Keys

from pages.base_page import BasePage


class MainPageLocators:
    BUTTON_ANIME = "//*[@class='nav-link']"
    BUTTON_MANGA = "//div[2]//ul[1]/li[2]/a"
    CHARACTERS = "Персонажи"
    CHARACTERS_XPATH = "//div[2]//ul[1]/li[3]/a"
    RANDOM_ANIME = 'Случайное аниме'
    SEARCH_STRING = "//div[2]//ul[2]/li[3]//input"
    BUTTON_SEARCH_STRING = "//*[@id='navbar-search']"
    GENRES = "//*[@id='filter']/div[2]//div[2]/div[2]/button"
    CHOOSE_GENRES = "//*[@id='filter']/div[2]//span[7]/span"
    TYPE = "//*[@id='filter']/div[2]//div[3]/div[2]/button"
    CHOOSE_TYPE = "//*[@id='filter']/div[2]//div[3]//label[1]/span"
    TYPE_OF_VOICE_ACTING = "//*[@id='filter']/div[2]//div[4]/div[2]/button"
    CHOOSE_VOICE_ACTING = "//*[@id='filter']/div[2]//div[4]//label[1]/span"
    SEARCH_BUTTON = "//*[@id='filter']/div[2]//div[8]/button"
    LINE_DATE = "//*[@id='slider-range']"
    TEXT_END_PAGE = "//*[@id='wrap']/div[7]/div/div/div/h2"
    ATTRIBUTE = '/html/head/link[2]'


class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def find_url_anime(self):
        base_page = BasePage(self.driver)
        return base_page.get_attribute(MainPageLocators.BUTTON_ANIME, 'href')

    def find_button_anime(self):
        base_page = BasePage(self.driver)
        return base_page.get_text(MainPageLocators.BUTTON_ANIME)

    def click_on_button_anime(self):
        base_page = BasePage(self.driver)
        return base_page.get_locator_xpath(MainPageLocators.BUTTON_ANIME).click()

    def click_on_button_characters(self):
        base_page = BasePage(self.driver)
        return base_page.get_locator_link_text(MainPageLocators.CHARACTERS).click()

    def click_button_random_anime(self):
        base_page = BasePage(self.driver)
        return base_page.get_locator_link_text(MainPageLocators.RANDOM_ANIME).click()

    def write_on_search_string(self, text):
        base_page = BasePage(self.driver)
        base_page.get_locator_xpath(MainPageLocators.BUTTON_SEARCH_STRING).click()
        base_page.send_keys(MainPageLocators.SEARCH_STRING, text)
        return base_page.send_keys(MainPageLocators.SEARCH_STRING, Keys.RETURN)

    def choose_anime_with_filters(self):
        base_page = BasePage(self.driver)
        base_page.get_locator_xpath(MainPageLocators.GENRES).click()
        base_page.get_locator_xpath(MainPageLocators.CHOOSE_GENRES).click()
        base_page.get_locator_xpath(MainPageLocators.TYPE).click()
        base_page.get_locator_xpath(MainPageLocators.CHOOSE_TYPE).click()
        base_page.get_locator_xpath(MainPageLocators.TYPE_OF_VOICE_ACTING).click()
        base_page.get_locator_xpath(MainPageLocators.CHOOSE_VOICE_ACTING).click()
        return base_page.get_locator_xpath(MainPageLocators.SEARCH_BUTTON).click()

    def search_anime_by_date(self):
        base_page = BasePage(self.driver)
        base_page.get_locator_xpath(MainPageLocators.LINE_DATE).click()
        return base_page.get_locator_xpath(MainPageLocators.SEARCH_BUTTON).click()

    def check_attribute(self):
        base_page = BasePage(self.driver)
        return base_page.get_attribute(MainPageLocators.ATTRIBUTE, "type")

    def send_clear(self):
        base_page = BasePage(self.driver)
        base_page.click_on(MainPageLocators.BUTTON_SEARCH_STRING)
        base_page.send_keys(MainPageLocators.SEARCH_STRING, "Магическая битва 2")
        base_page.clear_input(MainPageLocators.SEARCH_STRING)
        base_page.send_keys(MainPageLocators.SEARCH_STRING, "91 день")
        return base_page.send_keys(MainPageLocators.SEARCH_STRING, Keys.RETURN)

    def check_clicks(self):
        base_page = BasePage(self.driver)
        base_page.click_release(MainPageLocators.BUTTON_ANIME)
        base_page.double_click(MainPageLocators.BUTTON_MANGA)

    def check_keyboard_click(self):
        base_page = BasePage(self.driver)
        base_page.keyboard_click(MainPageLocators.BUTTON_ANIME)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def check_js_click(self):
        base_page = BasePage(self.driver)
        return base_page.click_by_js(MainPageLocators.CHARACTERS_XPATH)

    def check_cookie(self):
        cookie = {"name": "test", "value": "bar"}
        self.driver.add_cookie(cookie)
        cookies = self.driver.get_cookie("test")
        return cookies["name"] == cookie["name"]

    def wait_click(self):
        base_page = BasePage(self.driver)
        return base_page.wait_and_click(MainPageLocators.BUTTON_ANIME)

    def click_windows(self):
        base_page = BasePage(self.driver)
        main_window = self.driver.current_window_handle
        base_page.keyboard_click(MainPageLocators.BUTTON_ANIME)
        page_two = self.driver.current_window_handle
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])
        self.driver.close()
        self.driver.switch_to.window(windows[1])
