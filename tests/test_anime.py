import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from helper.helpers import scroll_to

@pytest.mark.button
def test_site_anime_url(driver_chrome):
    element = driver_chrome.find_element(By.XPATH, "//*[@class='nav-link']")
    element.click()
    assert driver_chrome.current_url == 'https://animego.org/anime'


def test_anime_attribute(driver_chrome):
    element = driver_chrome.find_element(By.XPATH, "//*[@class='nav-link']")
    assert element.get_attribute('href') in 'https://animego.org/anime'

@pytest.mark.button
def test_anime_char(driver_chrome):
    element = driver_chrome.find_element(By.LINK_TEXT, "Персонажи")
    element.click()
    assert driver_chrome.title == 'Список аниме персонажей'


def test_anime_scroll(driver_chrome):
    scroll_to(driver_chrome)
    time.sleep(6)


def test_anime_text(driver_chrome):
    element = driver_chrome.find_element(By.CSS_SELECTOR, '.nav-link')
    assert element.text == "Аниме"

@pytest.mark.parametrize('text', ["91 день", "магическая битва", "тетрадь смерти"])
def test_anime_search(driver_chrome, text):
    element_1 = driver_chrome.find_element(By.CSS_SELECTOR, '#navbar-search')
    element_1.click()
    element_2 = driver_chrome.find_element(By.CSS_SELECTOR, ".form-control-reset.w-100.text-placeholder-4")
    element_2.send_keys(text)
    element_2.send_keys(Keys.RETURN)
    assert driver_chrome.current_url != "https://animego.org/"


def test_anime_random(driver_chrome):
    element = driver_chrome.find_element(By.LINK_TEXT, 'Случайное аниме')
    element.click()
    assert driver_chrome.current_url != 'https://animego.org/'

@pytest.mark.login
def test_anime_login(driver_chrome):
    driver_chrome.get('https://animego.org/login')
    login = driver_chrome.find_element(By.CSS_SELECTOR, "#username")
    login.send_keys('stylebender')
    password = driver_chrome.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys('123443')
    button_login = driver_chrome.find_element(By.CSS_SELECTOR, "#_submit")
    button_login.click()
    assert driver_chrome.title == 'Вход'


def test_anime_video(driver_chrome):
    driver_chrome.get('https://animego.org/anime/magiya-i-muskuly-2-2493')
    element = driver_chrome.find_element(By.XPATH, "//*[@id='content']//div/ a/div[2]")
    element.click()
    time.sleep(4)

