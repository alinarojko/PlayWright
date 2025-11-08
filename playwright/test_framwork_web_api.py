import json
import pytest
from playwright.sync_api import Playwright, expect
from pageObjects.loginPage import LoginPage
from utils.apiBase import APIUtils

with open("playwright/data/credentials.json") as f:
    test_data = json.load(f)

user_credentials_list = test_data["user_credentials"]

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # Create order via API
    api_Utils = APIUtils()
    order_number = api_Utils.createOrder(playwright, user_credentials)

    # User Credentials
    user_email = user_credentials["user_email"]
    user_password = user_credentials["user_password"]

    # Login
    loginPage = LoginPage(page)
    loginPage.navigate()

    #Order history page
    dashBoardPage = loginPage.login(user_email, user_password)
    orderHistoryPage = dashBoardPage.selectOrdersNavigationLink()
    orderDetailsPage = orderHistoryPage.selectOrder(order_number)
    orderDetailsPage.verifyOrderMessage()

    context.close()
