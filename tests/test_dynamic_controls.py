from playwright.sync_api import Page, expect
from pages.dynamic_controls_page import DynamicControlsPage


def test_remove_checkbox(page: Page):
    controls = DynamicControlsPage(page)
    controls.open()
    controls.click_remove()
    expect(controls.checkbox()).to_have_count(0)


def test_enable_and_type_input(page: Page):
    controls = DynamicControlsPage(page)
    controls.open()
    controls.click_enable()
    controls.type_in_input("hello")
    expect(controls.input_field()).to_have_value("hello")
