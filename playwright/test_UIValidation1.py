from playwright.sync_api import Page, expect
def test_UIValidationDynamicScript(page:Pagfe):
    # IphoneX, Nokia Edge Add 2 items to the cart and bverify they are showing in the cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    page.locator("app-card").filter(has_text="iphone X").get_by_role("button").click()
    page.locator("app-card").filter(has_text="Nokia Edge").get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)


def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").click()
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        email = text.split(" ")[4]
        assert email == "mentor@rahulshettyacademy.com"

