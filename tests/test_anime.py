import pytest
from helper.helpers import scroll_to
from pages.anime_list_page import AnimeList
from pages.anime_page import AnimePage
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
