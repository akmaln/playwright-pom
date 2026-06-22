from playwright.sync_api import Page


class DropdownPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/dropdown")

    def dropdown(self):
        return self.page.locator("#dropdown")

    def select_an_option(self, option_text):
        self.dropdown().select_option(label=option_text)

    def currently_selected_option(self):
        return self.dropdown().locator("option[selected]").inner_text()
