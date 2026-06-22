from playwright.sync_api import Page


class DynamicControlsPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/dynamic_controls")

    def checkbox(self):
        return self.page.get_by_role("checkbox")

    def input_field(self):
        return self.page.locator("#input-example input")

    def click_remove(self):
        self.page.get_by_role("button", name="Remove").click()

    def click_add(self):
        self.page.get_by_role("button", name="Add").click()

    def click_enable(self):
        self.page.get_by_role("button", name="Enable").click()

    def click_disable(self):
        self.page.get_by_role("button", name="Disable").click()

    def type_in_input(self, text):
        self.input_field().fill(text)
