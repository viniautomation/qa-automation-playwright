# QA Automation with Python and Playwright

Automated software testing project using Python, Playwright and Pytest.

## About the Project

This project demonstrates automated testing of TodoMVC, a web application for managing tasks.

The goal is to validate application functionality, detect unexpected behavior and practice software quality assurance.

## Technologies

- Python
- Playwright
- Pytest
- Chromium
- GitHub

## Automated Test Cases

The project currently includes six automated tests:

1. **Create and Complete a Task** — Verifies task creation, completion and persistence after refreshing the page.
2. **Multiple Tasks** — Creates two tasks, marks them as completed and verifies their persistence.
3. **Delete a Task** — Deletes a task and verifies that the correct task remains.
4. **Check and Uncheck** — Tests changing a task's completion status.
5. **Empty Task Validation** — Verifies that the application prevents the creation of an empty task.
6. **Active Filter** — Verifies that only incomplete tasks appear when the Active filter is selected.

## How to Run

**1. Install the required packages**

`python -m pip install pytest-playwright`

**2. Install the Chromium browser**

`python -m playwright install chromium`

**3. Run the tests**

`python -m pytest test_todomvc.py -v`

To watch the browser execute the tests:

`python -m pytest test_todomvc.py --headed -v`

## Test Results

Latest local execution: 6 tests passed.

## Learning Objectives

This project is part of my practical training in QA Automation, focusing on:

- Automated functional testing
- Test assertions and validation
- Debugging and error investigation
- Browser automation
- Software quality assurance

## Application Under Test

[TodoMVC — Playwright Demo](https://demo.playwright.dev/todomvc/)

---

Developed by **viniautomation** as part of an ongoing QA Automation learning journey.
