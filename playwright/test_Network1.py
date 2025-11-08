import pytest
from playwright.sync_api import  Page, Playwright

fakePayloadOrderResponse = {"data": [], "message": "No Orders"}
# Verify the message "There are no orders" with mocking data

def intercept_response(route):
    route.fulfill(json=fakePayloadOrderResponse)


@pytest.mark.smoke
def test_Network1(page: Page):
    # Login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()

    # Order history page
    page.get_by_role("button", name="  ORDERS").click()
    orders_test = page.locator(".mt-4").text_content()
    print(orders_test)
