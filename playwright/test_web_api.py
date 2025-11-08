from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create order via API
    api_Utils = APIUtils()
    order_number = api_Utils.createOrder(playwright)

    print(f"order_number is {order_number}")

    #Login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()

    #Order history page
    page.get_by_role("button", name="  ORDERS").click()
    row = page.locator("tr").filter(has_text=order_number)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()
