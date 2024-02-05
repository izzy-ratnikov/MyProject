import pytest
from selenium.webdriver import Keys

from helper.helpers import scroll_to
from pages.anime_list_page import AnimeList
from pages.anime_page import AnimePage
from pages.base_page import BasePage
from pages.characters_page import Characters
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.manga_page import Manga


@pytest.mark.button
def test_site_anime_url(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.click_on_button_anime()


def test_anime_attribute(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.find_button_anime()


@pytest.mark.button
def test_anime_characters(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.click_on_button_characters()


def test_anime_scroll(driver_chrome):
    scroll_to(driver_chrome)


def test_anime_text(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.find_button_anime()


@pytest.mark.parametrize('text', ["91 день", "магическая битва", "тетрадь смерти"])
def test_anime_search(driver_chrome, text):
    main_page = MainPage(driver_chrome)
    main_page.write_on_search_string(text)


def test_anime_random(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.click_button_random_anime()


@pytest.mark.xfail(reason="fixing box 'login'")
def test_anime_login(driver_chrome):
    login_page = LoginPage(driver_chrome)
    login_page.login_box()


def test_anime_short_video(driver_chrome):
    anime_page = AnimePage(driver_chrome)
    anime_page.watch_trailer_anime()


def test_anime_filter(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.choose_anime_with_filters()


def test_anime_filter_by_date(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.search_anime_by_date()


def test_anime_related(driver_chrome):
    anime_page = AnimePage(driver_chrome)
    anime_page.related_anime()


def test_select_anime_in_list(driver_chrome):
    anime_list = AnimeList(driver_chrome)
    anime_list.choose_anime_from_list()


def test_choose_anime_character(driver_chrome):
    character = Characters(driver_chrome)
    character.choose_character_in_list()


def test_select_manga(driver_chrome):
    manga = Manga(driver_chrome)
    manga.choose_manga_in_list()


@pytest.mark.xfail(reason="AssertionError")
def test_choose_sorted_manga(driver_chrome):
    manga = Manga(driver_chrome)
    manga.sorted_manga()


def test_find_text(driver_chrome):
    driver_chrome.get("https://animego.org/anime/magicheskaya-bitva-2-2332")
    locator = "//*[@id='content']//div[2]/div[2]//h1"
    base_page = BasePage(driver_chrome)
    assert "Магическая битва 2" == base_page.get_text(locator)


def test_attribute(driver_chrome):
    locator = '/html/head/link[2]'
    base_page = BasePage(driver_chrome)
    assert "image/png" == base_page.get_attribute(locator, "type")


def test_send_clear(driver_chrome):
    locator = "/html/body/div[2]/header/nav/div/div/ul[2]/li[3]/div/form/div/div/input"
    l_2 = '//*[@id="navbar-search"]'
    base_page = BasePage(driver_chrome)
    base_page.click_on(l_2)
    base_page.send_keys(locator, "Магическая битва 2")
    base_page.clear_input(locator)
    base_page.send_keys(locator, "91 день")
    base_page.send_keys(locator, Keys.RETURN)
    assert driver_chrome.current_url == "https://animego.org/search/all?q=91+%D0%B4%D0%B5%D0%BD%D1%8C"


def test_click_release(driver_chrome):
    locator = "/html/body/div[2]/header/nav/div/div/ul[1]/li[1]/a"
    l_2 = "/html/body/div[2]/header/nav/div/div/ul[1]/li[2]/a"
    base_page = BasePage(driver_chrome)
    base_page.click_release(locator)
    base_page.double_click(l_2)
    assert driver_chrome.current_url == "https://animego.org/manga"


def test_keyboard_click(driver_chrome):
    locator = "/html/body/div[2]/header/nav/div/div/ul[1]/li[1]/a"
    base_page = BasePage(driver_chrome)
    base_page.keyboard_click(locator)
    windows = driver_chrome.window_handles
    driver_chrome.switch_to.window(windows[1])
    assert driver_chrome.current_url == "https://animego.org/anime"


def test_js_click(driver_chrome):
    locator = "/html/body/div[2]/header/nav/div/div/ul[1]/li[3]/a"
    base_page = BasePage(driver_chrome)
    base_page.click_by_js(locator)
    assert driver_chrome.current_url == "https://animego.org/characters"


def test_cookie(driver_chrome):
    driver_chrome.get("https://animego.org/")
    cookie = {"name": "test", "value": "bar"}
    driver_chrome.add_cookie(cookie)
    cookies = driver_chrome.get_cookie("test")
    assert cookies["name"] == cookie["name"]
