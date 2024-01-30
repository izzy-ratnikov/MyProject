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
    assert driver_chrome.current_url == "https://animego.org/search/all?q=91+день" or "https://animego.org/search/all?q=магическая+битва" or "https://animego.org/search/all?q=тетрадь+смерти"


def test_anime_random(driver_chrome):
    element = driver_chrome.find_element(By.LINK_TEXT, 'Случайное аниме')
    element.click()
    assert driver_chrome.find_element(By.CSS_SELECTOR, ".star-rating.mr-2")


@pytest.mark.xfail(reason="fixing box 'login'")
def test_anime_login(driver_chrome):
    driver_chrome.get('https://animego.org/login')
    login = driver_chrome.find_element(By.CSS_SELECTOR, "#username")
    login.send_keys('stylebender')
    password = driver_chrome.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys('123443')
    button_login = driver_chrome.find_element(By.CSS_SELECTOR, "#_submit")
    button_login.click()
    assert driver_chrome.current_url == 'https://animego.org/profile/'


def test_anime_short_video(driver_chrome):
    driver_chrome.get('https://animego.org/anime/magiya-i-muskuly-2-2493')
    element = driver_chrome.find_element(By.XPATH, "//*[@id='content']/div/div[3]/div/div[2]/div[2]/a")
    element.click()
    time.sleep(5)
    assert element.get_attribute('href') in '"https://www.youtube.com/embed/zk0YBvw53MI"'


def test_anime_filter(driver_chrome):
    element = driver_chrome.find_element(By.XPATH, "//*[@id='filter']/div[2]//div[2]/div[2]/button")
    element.click()
    element_2 = driver_chrome.find_element(By.XPATH, "//*[@id='filter']/div[2]//span[7]/span")
    element_2.click()
    element_3 = driver_chrome.find_element(By.XPATH, "//*[@id='filter']/div[2]//div[3]/div[2]/button")
    element_3.click()
    element_4 = driver_chrome.find_element(By.XPATH, "//*[@id='filter']/div[2]//div[3]//label[1]/span")
    element_4.click()
    element_5 = driver_chrome.find_element(By.XPATH, "//*[@id='filter']/div[2]//div[4]/div[2]/button")
    element_5.click()
    element_6 = driver_chrome.find_element(By.XPATH, "//*[@id='filter']/div[2]//div[4]//label[1]/span")
    element_6.click()
    element_7 = driver_chrome.find_element(By.XPATH, "//*[@id='filter']/div[2]//div[8]/button")
    element_7.click()
    assert driver_chrome.current_url == "https://animego.org/anime/filter/genres-is-mystery/type-is-tv/dubbing-is-anilibria/apply"


def test_anime_filter_by_date(driver_chrome):
    line_date = driver_chrome.find_element(By.XPATH, "//*[@id='slider-range']")
    line_date.click()
    element = driver_chrome.find_element(By.XPATH, "//*[@id='filter']/div[2]//div[8]/button")
    element.click()
    assert driver_chrome.current_url == "https://animego.org/anime/filter/year-from-1991/apply"
