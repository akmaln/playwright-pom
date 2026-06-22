from playwright.sync_api import Page, expect

def test_homepage_loads(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    expect(page).to_have_title("The Internet")
    expect(page.get_by_role("heading", name="Welcome")).to_be_visible()