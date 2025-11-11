import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from utils.apiBaseFramework import APIUtils
from pageObjects.loginPage import LoginPage

scenarios("../features/orderTransaction.feature")
@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse("place the item order with {user_name} and {password}"))
def place_item_order(playwright, user_name, password, shared_data):
    # Create order via API
    user_credentials = {"user_email": user_name, "user_password": password}
    api_Utils = APIUtils()
    order_number = api_Utils.createOrder(playwright, user_credentials)
    shared_data["order_number"] = order_number

@given("the user is on landing page")
def user_on_landing_page(page, shared_data):
    # Login
    loginPage = LoginPage(page)
    loginPage.navigate()
    shared_data['login_page'] = loginPage

@when(parsers.parse("I login to portal with {user_name} and {password}"))
def login_to_portal(user_name, password, shared_data):
    loginPage = shared_data['login_page']
    dashBoardPage = loginPage.login(user_name, password)
    shared_data['dashBoardPage'] = dashBoardPage

@when('navigate to orders page')
def navigate_to_order_page(shared_data):
    dashBoardPage = shared_data['dashBoardPage']
    orderHistoryPage = dashBoardPage.selectOrdersNavigationLink()
    shared_data['orderHistoryPage'] = orderHistoryPage

@when('select the orderId')
def select_order_id(shared_data):
    orderHistoryPage = shared_data['orderHistoryPage']
    order_number = shared_data["order_number"]
    orderDetailsPage = orderHistoryPage.selectOrder(order_number)
    shared_data['orderDetailsPage'] = orderDetailsPage

@then('order message is successfully displayed')
def confirm_success_message(shared_data):
    orderDetailsPage = shared_data['orderDetailsPage']
    orderDetailsPage.verifyOrderMessage()
