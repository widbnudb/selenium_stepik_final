import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='en',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=r'D:\Exe\chromedriver_win32\chromedriver.exe')
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()