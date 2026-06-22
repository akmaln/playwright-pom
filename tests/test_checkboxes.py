from playwright.sync_api import Page, expect
from pages.checkbox_page import CheckboxPage

def test_check_first_checkbox(page: Page):
    checkboxes = CheckboxPage(page)
    checkboxes.open()
    checkboxes.click_checkbox(1)
    expect(checkboxes.checkbox(1)).to_be_checked()
