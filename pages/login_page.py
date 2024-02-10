from pages.base_page import BasePage


class LoginPageLocators:
    LOGIN = "#username"
    PASSWORD = "#password"
    BUTTON_LOGIN = "#_submit"


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.driver.get('https://animego.org/login')

    def login_box(self):
        base_page = BasePage(self.driver)
        base_page.send_keys_css(LoginPageLocators.LOGIN, "stylebender")
        base_page.send_keys_css(LoginPageLocators.PASSWORD, '123443')
        base_page.click_on_css(LoginPageLocators.BUTTON_LOGIN)
