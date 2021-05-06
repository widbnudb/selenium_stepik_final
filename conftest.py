import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(executable_path=r'D:\Exe\chromedriver_win32\chromedriver.exe', options=options)
    yield browser
    browser.quit()

