Playwright Automation Framework

Python • Playwright • PyTest • API • BDD • Allure • Jenkins

A clean and lightweight test automation framework supporting UI, API and hybrid E2E flows.
Built for portfolio, real interview tasks, and CI/CD pipelines.

✨ Features

UI testing (Playwright sync API)

API testing (token auth, request context)

API → UI scenario chaining

Network mocking

BDD (pytest-bdd + Gherkin)

Page Object Model

Allure reports (screenshots, videos, traces on failure)

Jenkins pipeline ready

📁 Main Structure
PlayWright/
  ├── tests/
  ├── pageObjects/
  ├── utils/
  ├── features/
  ├── playwright/data/
  ├── conftest.py
  ├── pytest.ini
  └── requirements.txt

▶ Run Tests
pytest


With Allure:

pytest --alluredir=allure-results
allure serve allure-results


🛠 Stack

Python • Playwright • PyTest • Allure • Jenkins • BDD • POM • API Testing
