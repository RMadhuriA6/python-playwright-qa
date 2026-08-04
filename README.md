# Python + Playwright — QA Automation (Work in Progress)

Manual QA engineer (8 years, Selenium/Java background) learning Python and Playwright from scratch, building this repo as visible, incremental proof of work — not a finished framework, but a real, running log of progress.

## Background

Prior automation experience was in Java + Selenium + Cucumber (BDD, Page Object Model, data-driven `Scenario Outline` testing). This repo is a fresh build in Python + Playwright, starting from zero Python knowledge.

## What's in here so far

- **Python fundamentals**: variables, data types, strings, lists, dictionaries, tuples, sets, conditionals, loops, functions (including default/keyword arguments, nested scope), exception handling
- **Playwright setup**: environment installation (including resolving a real Windows/venv/compiler dependency issue with `greenlet`)
- **First automation scripts**:
  - Basic navigation and page-title verification
  - Locator strategies explored hands-on: `get_by_role`, `get_by_text`, `page.locator()` (CSS), `get_by_test_id()` — including debugging a real strict-mode duplicate-match error and a lazy-loaded element that didn't exist in the DOM until scrolled
  - A working **login flow** against [saucedemo.com](https://www.saucedemo.com/):
    - Positive path (`standard_user` / `secret_sauce`) → verifies successful navigation to the inventory page
    - Negative path (`locked_out_user`) → verifies the correct error message is shown, including tracking down a subtle bug where `get_by_test_id()` silently failed because the site uses a `data-test` attribute, not Playwright's default `data-testid`

## Tech stack

- Python 3.9
- Playwright (sync API)
- PyCharm

## Real bugs found and fixed along the way

This repo intentionally keeps evidence of debugging, not just clean final code — recognizing and fixing real issues is the point:

- `TypeError` from passing a tuple instead of separate positional arguments
- Silent bug from a list-aliasing mistake (`list1 = list2` vs `.copy()`)
- Wrong exception type caught (`TimeoutError` vs Playwright's own `TimeoutError`)
- Element not interactable due to lazy-loaded content (fixed with `page.mouse.wheel()`)
- `get_by_test_id()` silently finding nothing due to a non-default test-id attribute name

## What's next

- Refactor scripts into classes (Page Object Model)
- pytest integration and fixtures
- Parameterized, data-driven tests
- HTML test reporting
- Full POM framework

## Status

Actively in progress. This README will be updated as the framework grows.
