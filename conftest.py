import os
import pytest
import allure
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chromium",
                     help="chromium|firefox|webkit")
    parser.addoption("--url_name", action="store",
                     default="https://rahulshettyacademy.com/client",
                     help="base url")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Включаем запись видео и трейсов"""
    return {
        **browser_context_args,
        "record_video_dir": "videos/",
        "record_video_size": {"width": 1280, "height": 720}
    }


@pytest.fixture
def page(playwright, request):
    """Создание браузера и страницы Playwright"""
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

    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto(url_name)

    yield page

    # --- teardown ---
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Трейс (ZIP)
    trace_path = f"traces/{test_name}_{timestamp}.zip"
    context.tracing.stop(path=trace_path)
    if os.path.exists(trace_path):
        allure.attach.file(trace_path, name="Playwright Trace",
                           attachment_type="application/zip")

    # Видео
    video = page.video
    if video:
        video_path = video.path()
        if os.path.exists(video_path):
            allure.attach.file(video_path, name="Video",
                               attachment_type="video/mp4")

    context.close()
    browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Фиксируем статус выполнения теста"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def attach_on_failure(request, page):
    """При падении теста прикладываем:
       - скриншот
       - HTML страницы"""
    yield
    failed = False
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        failed = True
    if hasattr(request.node, "rep_setup") and request.node.rep_setup.failed:
        failed = True

    if failed:
        screenshot_path = f"screenshots/{request.node.name}.png"
        page.screenshot(path=screenshot_path, full_page=True)
        allure.attach.file(screenshot_path, name="Failure Screenshot",
                           attachment_type=allure.attachment_type.PNG)

        html_content = page.content()
        allure.attach(html_content, name="Page Source",
                      attachment_type=allure.attachment_type.HTML)
