from playwright.sync_api import Page, expect
from pages.basic_auth_page import BasicAuthPage


def test_basic_auth_success(page: Page):
    basic_auth = BasicAuthPage(page)
    basic_auth.open()
    expect(basic_auth.success_message()).to_contain_text("Congratulations")
