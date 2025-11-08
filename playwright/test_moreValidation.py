from playwright.sync_api import Page, expect, Dialog


def test_UIChecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

def test_allertBox(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.on("dialog",lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm")

# Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="top").click()

# Frame Handling
    pageFrame = page.frame_locator("iFrame Example")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscribers!")

# Web Table Handling - Check the price of rice is 37
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count()>0:
            colValue = i
            break

    riceRow = page.locator("th").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(colValue)).to_contain_text("37")

