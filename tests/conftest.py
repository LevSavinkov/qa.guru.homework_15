import pytest
from selene import browser


@pytest.fixture(scope="session")
def set_base_url():
    browser.config.base_url = "https://github.com"


@pytest.fixture(scope="function",
                params=[(1920, 1080), (1440, 900), (1280, 1024)],
                ids=["desktop_1920x1080", "desktop_1440x900", "desktop_1280x1024"])
def desktop_browser(request, set_base_url):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(scope="function",
                params=[(414, 896), (360, 640), (768, 1024)],
                ids=["iPhone_11_Pro_Max", "iPhone_SE", "iPad_Mini"])
def mobile_browser(request, set_base_url):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(scope="function",
                params=[(1920, 1080), (1440, 900), (360, 640), (768, 1024)],
                ids=["desktop_1920x1080", "desktop_1440x900", "mobile_360x640", "mobile_768x1024"])
def desktop_or_mobile_browser(request, set_base_url):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width >= 1024:
        yield "desktop"
    else:
        yield "mobile"
    browser.quit()
