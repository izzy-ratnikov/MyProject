import pytest
from helper.helpers import scroll_to
from pages.anime_list_page import AnimeList
from pages.anime_page import AnimePage, AnimePageLocators
from pages.base_page import BasePage
from pages.characters_page import Characters
from pages.login_page import LoginPage
from pages.main_page import MainPage, MainPageLocators
from pages.manga_page import Manga


@pytest.mark.button
def test_site_anime_url(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.click_on_button_anime()
    assert driver_chrome.current_url == 'https://animego.org/anime'


def test_anime_attribute(driver_chrome):
    main_page = MainPage(driver_chrome)
    assert main_page.find_url_anime() in 'https://animego.org/anime'


@pytest.mark.button
def test_anime_characters_title(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.click_on_button_characters()
    assert driver_chrome.title == 'Список аниме персонажей'


def test_anime_scroll(driver_chrome):
    scroll_to(driver_chrome)
    base_page = BasePage(driver_chrome)
    assert base_page.get_text(MainPageLocators.TEXT_END_PAGE) == "На AnimeGO – только бесплатные аниме без регистрации"


def test_anime_text(driver_chrome):
    main_page = MainPage(driver_chrome)
    assert main_page.find_button_anime() == "Аниме"


@pytest.mark.parametrize('text', ["91 день", "магическая битва", "тетрадь смерти"])
def test_anime_search(driver_chrome, text):
    main_page = MainPage(driver_chrome)
    main_page.write_on_search_string(text)
    assert driver_chrome.current_url == "https://animego.org/search/all?q=91+день" or "https://animego.org/search/all?q=магическая+битва" or "https://animego.org/search/all?q=тетрадь+смерти"


def test_anime_random(driver_chrome):
    main_page = MainPage(driver_chrome)
    base_page = BasePage(driver_chrome)
    main_page.click_button_random_anime()
    assert base_page.get_locator_css(AnimePageLocators.STAR_RATING)


@pytest.mark.xfail(reason="fixing box 'login'")
def test_anime_login(driver_chrome):
    login_page = LoginPage(driver_chrome)
    login_page.login_box()
    assert driver_chrome.current_url == 'https://animego.org/profile/'


def test_anime_short_video(driver_chrome):
    anime_page = AnimePage(driver_chrome)
    assert anime_page.watch_trailer_anime() in "https://www.youtube.com/embed/zk0YBvw53MI"


def test_anime_filter(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.choose_anime_with_filters()
    assert driver_chrome.current_url == "https://animego.org/anime/filter/genres-is-mystery/type-is-tv/dubbing-is-anilibria/apply"


def test_anime_filter_by_date(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.search_anime_by_date()
    assert driver_chrome.current_url == "https://animego.org/anime/filter/year-from-1991/apply"


def test_anime_related(driver_chrome):
    anime_page = AnimePage(driver_chrome)
    anime_page.related_anime()
    assert driver_chrome.current_url == "https://animego.org/anime/agent-vremeni-1780"


def test_select_anime_in_list(driver_chrome):
    anime_list = AnimeList(driver_chrome)
    anime_list.choose_anime_from_list()
    assert driver_chrome.current_url == "https://animego.org/anime/buttigiri-2523"


def test_choose_anime_character(driver_chrome):
    character = Characters(driver_chrome)
    character.choose_character_in_list()
    assert driver_chrome.current_url == "https://animego.org/character/35600-watanabe-hitachi"


def test_select_manga(driver_chrome):
    manga = Manga(driver_chrome)
    manga.choose_manga_in_list()
    assert driver_chrome.current_url == "https://animego.org/manga/keyon-shaffl-1795"


def test_choose_sorted_manga(driver_chrome):
    manga = Manga(driver_chrome)
    manga.sorted_manga()
    assert driver_chrome.current_url == "https://animego.org/manga?sort=r.rating&direction=desc"


def test_find_text(driver_chrome):
    anime_page = AnimePage(driver_chrome)
    assert "Магическая битва 2" == anime_page.find_name_anime()


def test_attribute(driver_chrome):
    main_page = MainPage(driver_chrome)
    assert main_page.check_attribute() == "image/png"


def test_send_clear(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.send_clear()
    assert driver_chrome.current_url == "https://animego.org/search/all?q=91+%D0%B4%D0%B5%D0%BD%D1%8C"


def test_clicks(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.check_clicks()
    assert driver_chrome.current_url == "https://animego.org/manga"


def test_keyboard_click(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.check_keyboard_click()
    assert driver_chrome.current_url == "https://animego.org/anime"


def test_js_click(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.check_js_click()
    assert driver_chrome.current_url == "https://animego.org/characters"


def test_cookie(driver_chrome):
    main_page = MainPage(driver_chrome)
    assert main_page.check_cookie()


def test_wait_and_click(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.wait_click()
    assert driver_chrome.current_url == "https://animego.org/anime"


def test_windows(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.click_windows()
    assert driver_chrome.current_url == "https://animego.org/anime"
