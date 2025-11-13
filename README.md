🎯 Python Playwright Automation Framework
PyTest • Playwright • API Testing • BDD • Allure Reporting • Jenkins CI/CD

📌 Overview
This repository contains a fully configured end-to-end Test Automation Framework built with:

Playwright (UI + API)
PyTest
PyTest-BDD
Allure Reporting
Jenkins CI/CD Pipeline

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
├── pageObjects/                    # Page Object Model classes
│   ├── loginPage.py
│   ├── dashboardPage.py
│   ├── orderHistoryPage.py
│   └── orderDetailsPage.py
│
├── utils/
│   ├── apiBaseFramework.py         # API utils (token + order creation)
│   └── apiBase.py                  # API helper for browser session injection
│
├── playwright/data/
│   └── credentials.json            # Test credentials for parametrized tests
│
├── features/
│   └── orderTransaction.feature    # BDD Gherkin scenario
│
├── tests/
│   ├── test_Network1.py            # Mocking API response
│   ├── test_Network2.py            # URL interception / negative mocks
│   ├── test_framework_web_api.py   # Full E2E UI+API test
│   ├── test_pytest_bddTest.py      # BDD test implementation
│   └── test_web_api.py             # Pure API-to-UI flow
│
├── allure-results/                 # Generated automatically
└── allure-report/                  # Generated automatically


🧪 Testing Capabilities
✔ UI testing (Playwright sync API)

Page navigation
User login
Order list and order details validation
Element assertions
Synchronization via locators

✔ API testing
Implemented via playwright.request.new_context():
Login via API
Authorization token extraction
Creating an order via API before running UI flow
Injecting token into browser sessionStorage/localStorage

Used in:
APIUtils.createOrder()
APIUtils.getToken()

✔ Network Mocking
Examples include:
Replacing backend order response
Returning fake payload
Modifying request URL dynamically

Used in:
test_Network1.py
test_Network2.py

✔ BDD (pytest-bdd)
Gherkin scenario:
Given place the item order with <user_name> and <password>
When I login to portal…
Then order message is successfully displayed

BDD implementation file:
test_pytest_bddTest.py


🧩 Fixtures & Test Infrastructure
🔧 conftest.py provides:

Browser initialization
Context creation with:
video recording
tracing (snapshots, screenshots, sources)
Auto-capture on failure:
screenshots
HTML source
video
trace .zip

Configurable command-line arguments:
--browser_name chromium|firefox|webkit
--url_name https://rahulshettyacademy.com/client

Allure attachments are added automatically via:
attach_on_failure()
pytest_runtest_makereport()

📊 Allure Reporting
Allure is configured via:
pytest.ini:
addopts = --alluredir=allure-results

Generated report:
allure generate allure-results -c -o allure-report

Attachments collected:
Screenshots on failure
Page HTML
Video (.webm → .mp4)
Playwright tracing ZIP

Jenkins triggers the same command inside the pipeline after tests finish.



🤖 Jenkins CI/CD Integration
Jenkins job uses Custom Workspace:
C:\Users\<user>\PycharmProjects\PlayWright

Build Step (Windows batch command):
cd C:\Users\<user>\PycharmProjects\PlayWright
call .venv\Scripts\activate
pytest

Post-build steps:
1️⃣ Generate Allure report:
C:\allure\allure-2.30.0\bin\allure.bat generate ^
C:\Users\<user>\PycharmProjects\PlayWright\allure-results ^
-c -o C:\Users\<user>\PycharmProjects\PlayWright\allure-report

2️⃣ Publish Allure Report plugin
Select Allure Report
Set Results Path = allure-results
Jenkins will display the report tab inside the job



▶ How to Run Tests Locally
1️⃣ Install dependencies:
pip install -r requirements.txt

2️⃣ Install Playwright browsers:
python -m playwright install

3️⃣ Run tests:
pytest --alluredir=allure-results

4️⃣ Generate Allure report:
allure generate allure-results -c -o allure-report
allure serve allure-results


📌 Technologies Used
Area	Tools
UI Automation	Playwright
API Testing	Playwright APIRequestContext
Test Runner	PyTest
BDD	pytest-bdd
Reporting	Allure Reporting
CI/CD	Jenkins
Pattern	Page Object Model (POM)
Language	Python
🏁 Final Notes


This project demonstrates:
Advanced Playwright automation skills
API + UI hybrid testing
BDD proficiency
Real CI/CD integration
Allure reporting with video, tracing and screenshots
Clean architecture suitable for scaling
