🎯 Python Playwright Automation Framework
PyTest • Playwright • API Testing • BDD • Allure Reporting • Jenkins CI/CD
📌 Overview

This repository contains a fully configured end-to-end Test Automation Framework built with:

Playwright (UI + API)

PyTest

pytest-bdd

Allure Reporting

Jenkins CI/CD

The framework supports:

✔ UI end-to-end flows
✔ API-driven test preparation (order creation via API)
✔ Network mocking
✔ Session injection
✔ BDD (Gherkin + pytest-bdd)
✔ Screenshots, videos & traces
✔ Full Allure integration
✔ Jenkins pipeline execution
✔ Parameterized tests & fixtures
✔ Page Object Model (POM)

It is designed to demonstrate real automation engineering skills for interviews and portfolio projects.

📁 Project Structure
PlayWright/
│
├── conftest.py                     # Global fixtures: browser, tracing, video, Allure attachments
├── pytest.ini                      # PyTest config (Allure dir + markers)
├── requirements.txt                # Project dependencies
│
├── pageObjects/
│   ├── loginPage.py
│   ├── dashboardPage.py
│   ├── orderHistoryPage.py
│   └── orderDetailsPage.py
│
├── utils/
│   ├── apiBaseFramework.py         # API utils (token + order creation)
│   └── apiBase.py                  # Helper for session injection
│
├── playwright/
│   └── data/
│       └── credentials.json        # Credentials for parametrized tests
│
├── features/
│   └── orderTransaction.feature    # BDD Gherkin scenario
│
├── tests/
│   ├── test_Network1.py
│   ├── test_Network2.py
│   ├── test_framework_web_api.py
│   ├── test_pytest_bddTest.py
│   └── test_web_api.py
│
├── allure-results/                 # Generated automatically
└── allure-report/                  # Generated automatically

🧪 Testing Capabilities
✔ UI Testing (Playwright)

Page navigation

User login

Order validation

Assertions

Locator-based synchronization

✔ API Testing

Implemented via:

playwright.request.new_context()


Capabilities:

Login via API

Token extraction

Order creation before UI test

Session injection into browser

Used in:

APIUtils.createOrder()
APIUtils.getToken()

✔ Network Mocking

Examples:

Fake backend response

Modified payload

Redirected URL

Interception of API calls

Used in:

test_Network1.py
test_Network2.py

✔ BDD (pytest-bdd)

Gherkin example:

Given user logs in with valid credentials
When order is placed
Then confirmation message is displayed


BDD implementation:

test_pytest_bddTest.py

🧩 Fixtures & Test Infrastructure
conftest.py handles:

Browser initialization

Video recording

Playwright tracing

Automatic Allure attachments on failure:

screenshot

HTML source

video

trace.zip

Custom CLI args:

--browser_name chromium|firefox|webkit
--url_name https://rahulshettyacademy.com/client


Allure is integrated via:

pytest_runtest_makereport()

📊 Allure Reporting

Run tests:

pytest --alluredir=allure-results


Generate report:

allure generate allure-results -c -o allure-report
allure serve allure-results


Allure includes:

screenshots

videos

HTML dumps

tracing zip

🤖 Jenkins CI/CD Integration
Custom Workspace:
C:\Users\<user>\PycharmProjects\PlayWright

Build Step (Windows):
cd C:\Users\<user>\PycharmProjects\PlayWright
call .venv\Scripts\activate
pytest

Post-Build:
"C:\allure\allure-2.30.0\bin\allure.bat" generate ^
allure-results -c -o allure-report


Allure Report Plugin displays results in Jenkins UI.

▶ Run Tests Locally

Install dependencies:

pip install -r requirements.txt


Install Playwright browsers:

python -m playwright install


Run tests:

pytest


Run with Allure:

pytest --alluredir=allure-results
allure serve allure-results

🏁 Final Notes

This project demonstrates:

Advanced Playwright automation

API + UI hybrid testing

CI/CD integration

Professional test architecture

A complete reporting system
