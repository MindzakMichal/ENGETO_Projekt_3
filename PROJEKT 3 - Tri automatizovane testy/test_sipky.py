from playwright.sync_api import Page, expect

# TEST 1
# Open homepage, click Termínovka link, and verify correct URL
def test_terminovka_page(page: Page):
    page.goto("https://www.sipky.org/")
    terminovka_link = page.get_by_role("link", name="Termínovka")
    expect(terminovka_link).to_be_visible()
    terminovka_link.click()
    expect(page).to_have_url("https://www.sipky.org/?region=uso&page=terminovka")
   
# TEST 2
# Search for "finale", open the article, and verify correct article page URL
def test_search_button(page: Page):
    page.goto("https://sipky.org")
    search_input = page.locator("#search_text")
    expect(search_input).to_be_visible()
    search_input.fill("finale")
    page.locator("#quick_search_form input[type='submit']").click()
    article = page.get_by_role("link", name="ČDS CUP 2026 zná své vítěze").first
    expect(article).to_be_visible()
    article.click()
    expect(page).to_have_url("https://www.sipky.org/?region=olk&page=aktuality&article=20685")
    
# TEST 3
# Verify that clicking NSA logo opens a popup with correct URL
def test_nsa_popup(page: Page):
    page.goto("https://sipky.org")
    with page.expect_popup() as popup_info:
        page.locator("a:has(img[src='/images/content/narodni_sportovni_agentura.png'])").click()
    popup = popup_info.value
    expect(popup).to_have_url("https://nsa.gov.cz/")






    






