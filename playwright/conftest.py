import allure
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chromium",
                     help="chromium|firefox|webkit")
    parser.addoption("--url_name", action="store",
                     default="https://rahulshettyacademy.com/client",
                     help="base url")

@pytest.fixture
def page(playwright, request):
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")

    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise RuntimeError(f"Unknown browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()
    page.goto(url_name)
    yield page


    context.close()
    browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def attach_on_failure(request, page):
    yield
    failed = False
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        failed = True
    if hasattr(request.node, "rep_setup") and request.node.rep_setup.failed:
        failed = True

    if failed:
        png = page.screenshot(full_page=True)
        allure.attach(png, name="failure_screenshot",
                      attachment_type=allure.attachment_type.PNG)

        html = page.content()
        allure.attach(html, name="page_source",
                      attachment_type=allure.attachment_type.HTML)
