import time

import pytest


from helper.helpers import scroll_to
from pages.anime_page import AnimePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


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
    time.sleep(6)


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
