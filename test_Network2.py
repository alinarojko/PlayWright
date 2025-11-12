import time

from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils


# api call from the browser - api call contact server
def intercept_response(route):
    wrong_order_id = "690c6e4af669d6cb0a45e6d0"
    original_url = route.request.url
    print(f"ORIGINAL URL {original_url}")

    modified_url = original_url.replace(original_url.split("=")[-1], wrong_order_id)
    print(f"MODIFIED URL {modified_url}")
    route.continue_(url=modified_url)

def test_Network2(page: Page):
    # Login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("**/api/ecom/order/get-orders-details?id=*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()

    # Order history page
    page.get_by_role("button", name="  ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    page.wait_for_selector(".blink_me", timeout=15000)
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    get_token = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # script to inject token into the session local storage, injecting javascript
    page.add_init_script(f"window.localStorage.setItem('token', '{get_token}')")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="  ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
