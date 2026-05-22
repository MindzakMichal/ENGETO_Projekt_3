from playwright.sync_api import Page, expect, sync_playwright
import pytest


@pytest.fixture(scope="session")
def custom_page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=1600)
        page = browser.new_page()
        yield page


# TEST 1
# Otvorenie stranky a kontrola nadpisu
def test_terminovka_page(custom_page):
    custom_page.goto("https://www.sipky.org/")
    custom_page.click("#main_menu > tbody > tr > td:nth-child(3) > a")
    expect(custom_page).to_have_url("https://www.sipky.org/?region=uso&page=terminovka")
    heading = custom_page.locator("#main_menu > tbody > tr > td:nth-child(3) > a")
    expect(heading).to_have_text("Termínovka")

# TEST 2
# Vyhladavanie slova "finale"
def test_search_button(custom_page):
    custom_page.goto("https://sipky.org")
    search_input = custom_page.locator("#search_text")
    expect(search_input).to_be_visible()
    search_input.click()
    search_input.fill("finale")
    custom_page.wait_for_timeout(500)
    custom_page.locator("#quick_search_form > table > tbody > tr > td.submit > input").click()

# TEST 3
# Otvorenie NSA stranky v novom okne
def test_nsa_popup(custom_page):

    custom_page.goto("https://sipky.org")
    with custom_page.expect_popup() as popup_info:
        custom_page.click("body > div.page > div.page-body > div:nth-child(1) > div:nth-child(4) > div.body.center > a > img")
        popup = popup_info.value
        expect(popup).to_have_url("https://nsa.gov.cz/")






    






