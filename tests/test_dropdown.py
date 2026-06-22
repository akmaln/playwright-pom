import pytest
from playwright.sync_api import Page, expect
from pages.dropdown_page import DropdownPage


@pytest.mark.parametrize("option", ["Option 1", "Option 2"])
def test_selected_dropdown_option(page: Page, option):
    dropdown = DropdownPage(page)
    dropdown.open()
    dropdown.select_an_option(option)
    assert dropdown.currently_selected_option() == option
