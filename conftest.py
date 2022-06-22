import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def open_google():
    browser.open('https://google.com/ncr')


@pytest.fixture(autouse=True)
def window_size(open_google):
    browser.driver.set_window_size(width=1920, height=1080)
