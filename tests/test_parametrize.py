"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser

from src.pages.github import GithubPage

desktop = pytest.mark.parametrize('desktop_browser', [(1366, 768), (1280, 1024)],
                                  indirect=True,
                                  ids=['desktop_1366x768', 'desktop_1280x1024'])
mobile = pytest.mark.parametrize('mobile_browser', [(360, 640), (720, 1280)],
                                 indirect=True,
                                 ids=['Samsung_Galaxy_A10', 'Xiaomi_Redmi_Note_7'])

github_page = GithubPage()


@desktop
def test_github_desktop(desktop_browser):
    browser.open('/')
    github_page.go_to_sign_in_desktop()


@mobile
def test_github_mobile(mobile_browser):
    browser.open('/')
    github_page.go_to_sign_in_mobile()
