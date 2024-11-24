"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser

from src.pages.github import GithubPage

github_page = GithubPage()


def test_github_desktop(desktop_browser):
    browser.open('/')
    github_page.go_to_sign_in_desktop()


def test_github_mobile(mobile_browser):
    browser.open('/')
    github_page.go_to_sign_in_mobile()
