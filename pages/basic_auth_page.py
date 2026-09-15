from playwright.sync_api import Page


class BasicAuthPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, username="admin", password="admin"):
        self.page.goto(f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth")

    def success_message(self):
        return self.page.locator("p")
