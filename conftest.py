import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from api_client import ApiClient


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture
def dog_api():
    return ApiClient(base_address="https://dog.ceo/api/")
