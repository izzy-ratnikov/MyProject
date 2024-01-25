import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from help import scroll_to


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
def test_site_anime_url(driver_chrome):
    driver_chrome.get('https://animego.org/')
    element = driver_chrome.find_element(By.XPATH, "//*[@class='nav-link']")
    element.click()
    assert driver_chrome.current_url == 'https://animego.org/anime'


def test_anime_attribute(driver_chrome):
    driver_chrome.get('https://animego.org/')
    element = driver_chrome.find_element(By.XPATH, "//*[@class='nav-link']")
    assert element.get_attribute('href') in 'https://animego.org/anime'


def test_anime_char(driver_chrome):
    driver_chrome.get('https://animego.org/')
    element = driver_chrome.find_element(By.LINK_TEXT, "Персонажи")
    element.click()
    assert driver_chrome.title == 'Список аниме персонажей'


def test_anime_scroll(driver_chrome):
    driver_chrome.get('https://animego.org/')
    scroll_to(driver_chrome)
    time.sleep(6)


def test_anime_text(driver_chrome):
    driver_chrome.get('https://animego.org/')
    element = driver_chrome.find_element(By.CSS_SELECTOR, '.nav-link')
    assert element.text == "Аниме"


def test_anime_search(driver_chrome):
    driver_chrome.get('https://animego.org/')
    element_1 = driver_chrome.find_element(By.CSS_SELECTOR, '#navbar-search')
    element_1.click()
    element_2 = driver_chrome.find_element(By.CSS_SELECTOR, ".form-control-reset.w-100.text-placeholder-4")
    element_2.send_keys('Наруто')
    element_2.send_keys(Keys.RETURN)
    assert driver_chrome.current_url == "https://animego.org/search/all?q=%D0%9D%D0%B0%D1%80%D1%83%D1%82%D0%BE"


def test_anime_random(driver_chrome):
    driver_chrome.get('https://animego.org/')
    element = driver_chrome.find_element(By.LINK_TEXT, 'Случайное аниме')
    element.click()
    assert driver_chrome.current_url != 'https://animego.org/'


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
    element = driver_chrome.find_element(By.CSS_SELECTOR, ".video-item-icon.m-1.d-flex.align-items-center.justify-content-center")
    element.click()
    time.sleep(4)
