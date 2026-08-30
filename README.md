# Python + Playwright — Automation Framework (In Progress)

Manual QA engineer (8 years, Selenium/Java background) building a real Playwright + pytest automation framework from scratch — this repo tracks genuine, incremental progress, including real bugs found, real debugging, and real design decisions, not just a finished, polished product.

## Status as of Aug 30, 2026

**Done and stable:** Login page (full 12-case suite + edge cases), Products page (sort verification across all 4 directions, both label and underlying data), inheritance via `BasePage`, SQL-backed test data, HTML reporting.

**In progress:** Cart page, Checkout page, API testing, HTML reporting polish, and an optional pytest-bdd (Gherkin/BDD) layer once the core framework is complete.

## Architecture

```
framework/
├── pages/        <- locators ONLY, one class per page (object-repository style)
│   ├── base_page.py       <- shared BasePage: self.page, get_title(), get_url()
│   ├── login_page.py
│   ├── products_page.py
│   ├── main_header.py
│   └── burger_menu_page.py
├── actions/      <- methods that act on a page's locators (fill, click, sort)
├── utils/        <- reusable logic, e.g. SQLite data-reading functions
├── data/         <- test_data.db (SQLite) — real login and sort test data
├── tests/        <- actual pytest test files
└── reports/      <- generated HTML reports (gitignored, one kept as evidence — see below)
```

**Design choice, deliberately:** locators and actions are kept in *separate* classes (e.g. `LoginPage` holds locators, `LoginActions` performs the login) rather than combined into one class per page. This is a stricter variant of Page Object Model, closer to an HP ALM-style object repository from prior Selenium/Java work — a valid tradeoff prioritizing clear separation of concerns over fewer files.

`BasePage` provides shared, page-agnostic behavior (`self.page`, `get_title()`, `get_url()`) that every page class inherits via `super().__init__(page)`.

## Tech stack

- Python 3.9, Playwright (sync API), pytest
- pytest fixtures + `conftest.py` for shared browser setup
- `pytest.mark.parametrize` (including stacked decorators for multi-dimensional test combinations)
- SQLite (`sqlite3`) for test data, with parameterized queries
- pytest-html for reporting

## A real bug this framework caught

`problem_user` is one of saucedemo's six built-in accounts, documented to have broken product sorting. This framework's Products page suite runs the same sort-verification logic across multiple users (`standard_user`, `problem_user`) using stacked `parametrize` decorators — and it correctly, independently caught the bug:

- `standard_user`: all 4 sort directions pass.
- `problem_user`: 3 of 4 sort directions **fail**, exactly matching the documented, real issue.

**See the actual test report:** [`framework/reports/report.html`](framework/reports/report.html) — kept as a deliberate exception to the gitignored reports folder, specifically as evidence this framework detects real, known defects rather than just running green.

## 🐞 Debug Log — Real Bugs Found and Fixed

This repo keeps a running, categorized log of real issues hit during development — not just "it works now," but the symptom, what was tried and failed, the actual root cause, and the fix. A selection of the most instructive entries:

**Locators**
- `get_by_test_id()` silently found nothing despite a correct-looking value — it defaults to matching `data-testid`, but the site used `data-test`. Fixed with a raw CSS attribute selector instead of assuming the default attribute name.
- A locator matched two elements (`get_by_text` catching both a `<span>` and its parent `<a>`) — Playwright's strict mode correctly refused to guess, resolved by switching to a role-based locator.
- `select_option()` defaulted to matching on `value=` instead of `label=`, crashing on parentheses in a human-readable option name like `"Price (high to low)"`.

**Timing / Async**
- An element didn't exist in the DOM at all until a real scroll event fired (lazy-loading) — `count()` returned 0 even though the element existed manually. Fixed with `page.mouse.wheel()` to trigger genuine lazy-load behavior, not just `scroll_into_view_if_needed()`.
- Checked a page's title immediately after a click, before navigation had actually finished — read stale state. Root motivation for later adopting `expect()` over one-shot checks everywhere.

**CSS / Layout**
- A fixed-position header intercepted Playwright's coordinate-based clicks regardless of scroll position. Four hypotheses ruled out with direct evidence (`bounding_box()`, manual window resize, `page.pause()` inspection) before confirming `position: fixed` via DevTools and fixing it with `element.evaluate("el => el.click()")` — a native DOM click that bypasses simulated mouse coordinates entirely.

**Test Design / False Positives**
- A "PASSED" multi-tab test was checking the *wrong* page — `get_by_role(..., name="New Window")` matched via default substring behavior against the *original* tab's heading ("Opening a **new window**"). Fixed with `exact=True` plus a direct URL check on the correct tab.

**Python / OOP**
- `list1 = list2` shared the same underlying list instead of copying it (aliasing) — `.copy()` fixes it; the root cause is that variables hold references, not data.
- Three separate, deliberately-induced crashes while learning `self` — a bare local variable never attaches to an object unless explicitly written as `self.attribute = value`. Rebuilt correctly three times until the mechanism was fully internalized, not just memorized.
- `.append()` returns `None` (it mutates in place) — `my_list = my_list.append(x)` silently wipes the list after the first call.
- A parametrized sort test crashed with `TypeError: cannot unpack non-iterable NoneType Objects` on some cases but not others. Root cause: SQLite's `fetchall()` returned one-item tuples (`('Name (A to Z)',)`), not plain strings — a string-equality check inside the function silently never matched, falling through with no `return`. One case happened to pass anyway, because a *different*, more forgiving assertion method tolerated the wrong type by coincidence — a reminder that one passing case doesn't prove the data shape is correct. Fixed with a list comprehension (`[row[0] for row in cursor.fetchall()]`) to unwrap each tuple.

*Full log with symptom/attempted-fixes/root-cause/why-it-matters detail for every entry is tracked separately during development.*

## What's next

- Complete CartPage / CheckoutPage (with GitHub Copilot as a reviewed accelerator, now that the pages/actions pattern is well-proven)
- API testing (public test API, since saucedemo has no real backend)
- Full POM suite pass and framework polish
- Optional stretch: pytest-bdd (Gherkin/BDD layer) on top of the completed framework

## Status

Actively in progress, updated regularly as real work happens.
