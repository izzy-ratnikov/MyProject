from selenium.webdriver.common.by import By


class LoginPage:
    LOGIN = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "#_submit")

    def __init__(self, driver):
        self.driver = driver


    def login_box(self):
        self.driver.get('https://animego.org/login')
        login = self.driver.find_element(*LoginPage.LOGIN)
        login.send_keys('stylebender')
        password = self.driver.find_element(*LoginPage.PASSWORD)
        password.send_keys('123443')
        button_login = self.driver.find_element(*LoginPage.BUTTON_LOGIN)
        button_login.click()
        assert self.driver.current_url == 'https://animego.org/profile/'
