# Playwright POM Automation

[![tests](https://github.com/akmaln/playwright-pom/actions/workflows/tests.yml/badge.svg)](https://github.com/akmaln/playwright-pom/actions/workflows/tests.yml)

A UI automation suite built with **Python + Playwright** and **PyTest**, structured around the **Page Object Model (POM)**. This is a deliberate port of my Selenium POM suite ([**selenium-pom-automation**](https://github.com/akmaln/selenium-pom-automation)) — the same three pages and test scenarios, rebuilt in Playwright to demonstrate fluency in both frameworks and a working understanding of where they differ. Tests target [the-internet.herokuapp.com](https://the-internet.herokuapp.com).

## Tech Stack

- **Language:** Python 3.12
- **Browser automation:** Playwright
- **Test framework:** PyTest (via `pytest-playwright`)
- **Design pattern:** Page Object Model (POM)
- **CI:** GitHub Actions (runs the full suite on every push and PR)

## What This Demonstrates

- **Auto-waiting** — no explicit waits anywhere; Playwright waits for elements to be actionable on its own, eliminating the explicit-wait code (and a class of flaky tests) the Selenium version needed
- **Web-first assertions** — `expect(locator).to_*()` matchers that auto-retry until the condition holds or times out
- **Semantic locators** — `get_by_role`, with a scoped CSS fallback only where the page offers no semantic handle
- **Lean page objects** — page classes expose locators and perform actions; assertions live in the tests via `expect()`. No `BasePage` helper layer is needed, because a Playwright `Locator` already auto-waits and carries its own action methods
- **Parametrized tests** — `@pytest.mark.parametrize` driving the dropdown scenarios
- **Cross-browser by default** — the same tests run on Chromium, Firefox, and WebKit with no code changes (`--browser firefox`)
- **Trace-based debugging** — failures are captured as full, rewindable traces (DOM snapshots, timeline, network, console) via `--tracing retain-on-failure`

## Selenium -> Playwright: What Changed

| Concern | Selenium version | Playwright version |
|---|---|---|
| Waiting | `WebDriverWait` + expected conditions on every interaction | Auto-waiting built into actions and assertions |
| Assertions | Plain `assert` on one-shot booleans | `expect()` web-first matchers that auto-retry |
| Locators | XPath through the DOM | Semantic (`get_by_role`), CSS only as fallback |
| Driver setup | Custom `driver` fixture in `conftest.py` | Built-in `page` fixture from `pytest-playwright` |
| Shared helpers | `BasePage` wrapping waits and actions | Not needed — the `Locator` provides both |
| Screenshots / debugging | Custom screenshot-on-failure hook | Built-in trace viewer |

## Projects

| Project | Page Under Test | Concepts |
|---|---|---|
| **Checkboxes** | `/checkboxes` | Positional locators (`nth`), `.check()` / `.is_checked()` |
| **Dropdown** | `/dropdown` | `.select_option()`, parametrized scenarios, label-vs-value assertions |
| **Dynamic Controls** | `/dynamic_controls` | Auto-waiting through async DOM changes, `.fill()` waiting for an editable field |
| **Homepage** | `/` | Smoke test — page load and heading visibility |

## Project Structure

```
playwright-pom/
├── .github/
│   └── workflows/
│       └── tests.yml
├── pages/
│   ├── __init__.py
│   ├── checkbox_page.py
│   ├── dropdown_page.py
│   └── dynamic_controls_page.py
├── tests/
│   ├── __init__.py
│   ├── test_checkboxes.py
│   ├── test_dropdown.py
│   ├── test_dynamic_controls.py
│   └── test_homepage.py
├── README.md
└── requirements.txt
```

## Setup

```bash
# Clone and enter the repo
git clone https://github.com/akmaln/playwright-pom.git
cd playwright-pom

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install the browser binaries Playwright drives
playwright install
```

> The `playwright install` step is specific to Playwright — unlike Selenium, Playwright ships and manages its own browser builds rather than using the one installed on your machine.

## Running the Tests

```bash
# Run everything (headless, Chromium)
pytest

# Watch the browser run
pytest --headed

# Slow down each action to observe behavior
pytest --headed --slowmo 800

# Run on a different browser engine
pytest --browser firefox

# Capture a debuggable trace only when a test fails
pytest --tracing retain-on-failure
```

To open a captured trace:

```bash
playwright show-trace test-results/<test-folder>/trace.zip
```

## Notes

The suite is intentionally lean: no `conftest.py` is required, because `pytest-playwright` provides the `page` fixture, and failure debugging is handled by the built-in trace viewer rather than custom screenshot code. Much of the scaffolding the Selenium version maintained by hand is absorbed by the framework here — which is itself a large part of Playwright's appeal.