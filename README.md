# Automated Tests – sipky.org (Playwright)

# Project Overview
This project contains automated UI tests for the website https://www.sipky.org using Playwright and Pytest.

The tests verify basic functionality such as navigation, search, and popup handling.

---

# Installation
First, install the required Python dependencies:
python -m pip install -r requirements.txt

Then install Playwright browsers:
python -m playwright install

---

# Running Tests
Run all tests:
python -m pytest test_sipky.org

Run a specific test:
python -m pytest test_sipky.py::test_terminovka_page

---

# Technologies Used
Python
Pytest
Playwright
pytest-playwright

---

# Test Descriptions
1. test_terminovka_page
- Opens the homepage
- Clicks on the "Termínovka" link
- Verifies the correct URL is loaded

2. test_search_button
- Searches for the term "finale"
- Opens the found article
- Verifies the correct article URL
  
3. test_nsa_popup
- Clicks on the NSA banner/logo
- Opens a popup window
- Verifies the correct popup URL

---

# Notes
- Tests use the Playwright page fixture provided by pytest-playwright
- Browser runs in headless mode by default
- Selectors are designed to be as stable as possible

