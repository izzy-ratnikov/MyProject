from selenium.webdriver.common.by import By


class Characters:
    SELECT_CHARACTER = (By.XPATH, "//*[@id='anime-list-container']/div[1]//div[2]/h3/a")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://animego.org/characters")

    def choose_character_in_list(self):
        element = self.driver.find_element(*Characters.SELECT_CHARACTER)
        element.click()
        assert self.driver.current_url == "https://animego.org/character/35600-watanabe-hitachi"
