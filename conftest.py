import os
import pytest
import allure
from datetime import datetime
from allure_commons.types import AttachmentType

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "record_video_dir": "videos/",
        "record_video_size": {"width": 1280, "height": 720}
    }

@pytest.fixture
def page(playwright, request):
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    try:
        yield page

    finally:
        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # ---------------- TRACE ----------------
        trace_path = f"traces/{test_name}_{timestamp}.zip"
        context.tracing.stop(path=trace_path)

        if os.path.exists(trace_path):
            allure.attach.file(
                trace_path,
                name="Playwright Trace",
                attachment_type=AttachmentType.TEXT   # universal safe type
            )

        # ---------------- VIDEO ----------------
        video = page.video
        if video:
            video_path = video.path()

            try:
                page.close()
                context.close()
            except:
                pass

            if os.path.exists(video_path):
                allure.attach.file(
                    video_path,
                    name="Video",
                    attachment_type=AttachmentType.TEXT   # safe fallback
                )

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(autouse=True)
def attach_on_failure(request, page):
    yield

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_path = f"screenshots/{request.node.name}.png"
        page.screenshot(path=screenshot_path, full_page=True)

        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=AttachmentType.PNG
        )

        html = page.content()
        allure.attach(
            html,
            name="HTML Snapshot",
            attachment_type=AttachmentType.HTML
        )
