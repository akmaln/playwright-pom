# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A UI automation suite (Python + Playwright + PyTest) built around the Page Object Model, targeting the live public site [the-internet.herokuapp.com](https://the-internet.herokuapp.com). It's a deliberate port of a Selenium suite ([selenium-pom-automation](https://github.com/akmaln/selenium-pom-automation)) — same three pages/scenarios, rebuilt to lean on Playwright's built-in capabilities instead of hand-rolled scaffolding.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows (this repo's dev environment)
pip install -r requirements.txt
playwright install              # installs Playwright's own browser binaries
```

## Commands

```bash
pytest                                  # run everything, headless, Chromium
pytest --headed                         # watch the browser run
pytest --headed --slowmo 800            # slow down actions to observe
pytest --browser firefox                # run on a different engine (webkit also works)
pytest --tracing retain-on-failure      # capture a rewindable trace only on failure
pytest tests/test_dropdown.py           # run a single file
pytest tests/test_checkboxes.py::test_check_first_checkbox   # run a single test
playwright show-trace test-results/<test-folder>/trace.zip   # open a captured trace
```

CI (`.github/workflows/tests.yml`) runs `pytest -v` against Chromium only, on every push/PR to `main`.

## Architecture

- **No `conftest.py` and no `BasePage`.** `pytest-playwright` supplies the `page` fixture directly, and a Playwright `Locator` already auto-waits and carries its own action methods, so there's no shared driver-setup or wait-wrapper layer to maintain.
- **Page objects (`pages/`) expose locators and actions only** — e.g. `CheckboxPage.checkbox(number)`, `.click_checkbox(number)`. They do not assert.
- **Assertions live in the tests (`tests/`)**, using `expect(locator).to_*()` web-first matchers (auto-retrying) rather than one-shot `assert` on booleans, except where a plain value comparison is clearer (e.g. `test_dropdown.py` asserts on `currently_selected_option()` text directly).
- **Locator strategy:** prefer semantic locators (`get_by_role`), falling back to scoped CSS (`#dropdown`, `#input-example input`) only where the page under test offers no semantic handle.
- Each page object's `open()` navigates directly to its hardcoded URL on `the-internet.herokuapp.com` — there's no shared base-URL config.
- One test file has no matching page object: `test_homepage.py` is a standalone smoke test that drives `page` directly rather than through a POM class — keep it that way, it's intentionally minimal.

## Adding a new page/scenario

Follow the existing three as the template: create `pages/<name>_page.py` with an `__init__(self, page)`, `open()`, and locator/action methods; add `tests/test_<name>.py` that instantiates the page object and asserts via `expect()`.
