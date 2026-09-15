from playwright.sync_api import Page


class CheckboxPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")

    def checkbox(self, number):
        return self.page.locator("#checkboxes").get_by_role("checkbox").nth(number - 1)

    def click_checkbox(self, number):
        self.checkbox(number).check()

    def checkbox_is_selected(self, number):
        return self.checkbox(number).is_checked()
